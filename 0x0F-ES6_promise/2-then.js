export default function handleResponseFromAPI(promise) {
    promise
	.then(() => {
		console.log({status: 200, body: 'Success'})
	    return ({ status: 200, body: 'Success' });
	})
    .catch(() => {
	    return (new Error())
	})
    .then(() => {
	    console.log("Got a response from the API");
	});
}
