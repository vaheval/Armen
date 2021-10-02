<?php

// Routing class

class Route {

	public static function buildRoute() {

		//controller, model and action by default
		$controllerName = "IndexController";
		$modelName = "IndexModel";
		$action = "index";

		$request_uri = explode("/", $_SERVER['REQUEST_URI']);

		//Define controller and model
		if($request_uri[1]) {
			$fileName = CONTROLLER_PATH . ucfirst($request_uri[1]. "Controller") . ".php";
			if(is_file($fileName)){
				$controllerName = ucfirst($request_uri[1]. "Controller");
				$modelName = ucfirst($request_uri[1]. "Model");
			}
		}

		require_once CONTROLLER_PATH . $controllerName . ".php";
		require_once MODEL_PATH . $modelName . ".php";

		if(isset($request_uri[2])) {
			if(function_exists($request_uri[2]))
			$action = $request_uri[2];
		}

		$controller = new $controllerName();
		$controller->$action();
	}
}