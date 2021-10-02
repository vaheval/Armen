<?php

class Payment extends Customer {

	private $amount;

	public function __construct($firstname, $lastname){
		parent::__construct($firstname, $lastname);
	}

	public function getPaymentData(){
		return [
			'amount' => $this->amount
		];
	}

	public function setPaymentData($data){
		$this->amount = $data;
	}
}