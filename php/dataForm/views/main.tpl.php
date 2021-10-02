 <!DOCTYPE html>
<html>
	<head>
	   <meta charset="utf-8">
	   <!-- <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous"> -->
	   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
	   <title><?php echo $pageData['title']; ?></title>
	</head>
	<body>
		<div class="container mt-5">
			<div class="row">
				<div class="col-md-4"> </div>
				<div class="col-md-4">
					<h4 class="text-center">FORM OF PAYMENT</h4>
					<form action="./payment" method="post">
						<div class="mb-3">
						   <label for="name" class="form-label">First Name:</label>
						   <input required type="name" name="firstname" class="form-control" id="firstname" placeholder="First Name">
						</div>
						<div class="mb-3">
						   <label for="lastname" class="form-label">Last Name:</label>
						   <input required type="name" name="lastname" class="form-control" id="lastname" placeholder="Last Name">
						</div>
						<div class="mb-3">
						   <label for="number" class="form-label">Amount:</label>
						   <input required type="number" name="amount" class="form-control" id="amount" placeholder="Amount">
						</div>
						<button type="submit" class="btn btn-info">Send</button>
					</form>
				</div>
				<div class="col-md-4"> </div>
			</div>
		</div>
	</body>
</html>