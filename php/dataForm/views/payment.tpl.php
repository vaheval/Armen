<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
	   	<title>Test Task</title>
		<script>
			if ( window.history.replaceState ) {
			  window.history.replaceState( null, null, window.location.href );
			}
		</script>
	</head>
	<body>
		<div class="container mt-5">
			<h4 class="text-center">AMOUNTS</h4>
			<table class="table table-striped table-hover">
				<thead>
					<tr>
						<th scope="col">#</th>
						<th scope="col">First Name</th>
						<th scope="col">Last Name</th>
						<th scope="col">Amount</th>
					</tr>
				</thead>
				<tbody>
					<?php foreach ($pageData as $key => $row) :?>
					    <tr class="item_row">
				            <td><?php echo $key+1 ?></td>
				            <td> <?php echo $row['firstname'] ?></td>
				            <td> <?php echo $row['lastname'] ?></td>
				            <td> <?php echo $row['amount'] ?></td>
					    </tr>
					<?php endforeach;?>	
				</tbody>
			</table>
			<a href="/" class="btn btn-primary mb-5 mt-5" type="button">GO TO PAYMENT</a>
		</div>
	</body>
</html>