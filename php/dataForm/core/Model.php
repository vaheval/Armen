<?php

class Model {
	protected $db = null;

	public function __construct() {
		$database = new DB();
		$this->db = $database->connToDB();
	}
}