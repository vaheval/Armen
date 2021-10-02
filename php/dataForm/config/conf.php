<?php
	define("DOCUMENT_ROOT", $_SERVER['DOCUMENT_ROOT']);
	define("CONTROLLER_PATH", DOCUMENT_ROOT. "/controllers/");
	define("MODEL_PATH", DOCUMENT_ROOT. "/models/");
	define("VIEW_PATH", DOCUMENT_ROOT. "/views/");
	define("CORE_PATH", DOCUMENT_ROOT. "/core/");

	require_once("db.php");

	spl_autoload_register(function ($class_name) {
	    include_once CORE_PATH . $class_name . '.php';
	});

	$route = new Route();
	$route->buildRoute();