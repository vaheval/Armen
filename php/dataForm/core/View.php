<?php

class View {

	public function render($tpl, $pageData) {
		include DOCUMENT_ROOT. $tpl;
	}
}