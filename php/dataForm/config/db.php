<?php

// Configure DB class

class DB{

	const USER = "b694834e980240";
	const PASS = "4852ebea";
	const HOST = "us-cdbr-east-04.cleardb.com";
	const DB = "heroku_ac84991350bd290";

	public static function connToDB() {

		$user = self::USER;
		$pass = self::PASS;
		$host = self::HOST;
		$db = self::DB;

		try {
		    $conn = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
		    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
		}
		catch(PDOException $e){
		  echo $e->getMessage();                         
		}
		return $conn;
	}
}