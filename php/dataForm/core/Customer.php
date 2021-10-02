<?php

class Customer {

	private $firstname;
	private $lastname;

	public function __construct($firstname, $lastname) {
		$this->firstname = $firstname;
		$this->lastname = $lastname;
	}

	public function getCustomerData(){
		return [
			"firstname" => $this->firstname,
			"lastname" => $this->lastname
		];
	}	
}