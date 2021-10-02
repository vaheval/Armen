 <!--  Model payment insert data into db and select it

  DB tables structure

	describe customers
  +-----------+--------------+------+-----+---------+----------------+
  | Field     | Type         | Null | Key | Default | Extra          |
  +-----------+--------------+------+-----+---------+----------------+
  | id        | int          | NO   | PRI | NULL    | auto_increment |
  | FirstName | varchar(255) | NO   |     | NULL    |                |
  | LastName  | varchar(255) | NO   |     | NULL    |                |
  +-----------+--------------+------+-----+---------+----------------+ 

  describe amounts
	+-------------+------+------+-----+---------+----------------+
	| Field       | Type | Null | Key | Default | Extra          |
	+-------------+------+------+-----+---------+----------------+
	| id          | int  | NO   | PRI | NULL    | auto_increment |
	| customer_id | int  | NO   | MUL | NULL    |                |
	| Amount      | int  | YES  |     | NULL    |                |
	+-------------+------+------+-----+---------+----------------+
 -->


<?php

	class PaymentModel extends Model {

		const CUSTOMERS_TABLE = "customers";
		const AMOUNTS_TABLE = "amounts";

		//insert data into table customers
		public function insertIntoCostomers($data){
			$table = self::CUSTOMERS_TABLE;
			$sql = "INSERT INTO $table (FirstName, LastName) VALUES (:firstname, :lastname)";
			$stmt = $this->db->prepare($sql);
			$stmt->execute($data);
		}

		//insert data into table paymets
		public function insertIntoPayments($data){
			$id = $this->db->lastInsertId();
			$data += array("customer_id" => $id);
			$table = self::AMOUNTS_TABLE;
			$sql = "INSERT INTO $table (customer_id, Amount) VALUES (:customer_id, :amount)";
			$stmt = $this->db->prepare($sql);
			$stmt->execute($data);
		}

		//select data from customers and payment tables.
		public function selectDataFromTables(){

			$data = array();

			$c = self::CUSTOMERS_TABLE;
			$a = self::AMOUNTS_TABLE;
			$sql = "SELECT ${c}.FirstName, ${c}.LastName, ${a}.Amount FROM customers LEFT JOIN amounts ON customers.id = amounts.customer_id";
			foreach($this->db->query($sql) as $row){
				$data[] = array(
					'firstname' => $row['FirstName'],
					'lastname' => $row['LastName'],
					'amount' => $row['Amount']
				);
			}

			return $data;
		}
	}
