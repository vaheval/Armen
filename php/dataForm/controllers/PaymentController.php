<?php

// Payment Controller

class PaymentController extends Controller {

	private $pageTpl = '/views/payment.tpl.php';

	public function __construct() {
		$this->model = new PaymentModel();
		$this->view = new View();
	}

	public function index() {
		if(!isset($_POST['firstname'])) {
			header('Location: /');
			exit();
		}
		//Class Payment extends Customer
		$payment = new Payment($_POST['firstname'], $_POST['lastname']);
		$payment->setPaymentData($_POST['amount']);

		//Data for inset into db in table customers
		$customer = $payment->getCustomerData();

		//Data for inset into db in table customers
		$amount = $payment->getPaymentData();

		//Insert data into db
		$this->model->insertIntoCostomers($customer);
		$this->model->insertIntoPayments($amount);

		//Select data from table and store in pageData for show in page
		$this->pageData = $this->model->selectDataFromTables();

		//rendeer view
		$this->view->render($this->pageTpl, $this->pageData);
	}
}