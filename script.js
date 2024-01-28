function submitRating() {
    // Get form data
    const rating = document.getElementById('rating').value;
    const description = document.getElementById('description').value;

    // Prepare data object
    const data = {
        rating: rating,
        description: description,
        lawyer_id: 5,
    };

    // Fetch options
    const options = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin':'*',
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTcsImVtYWlsIjoibWFtZXJpbW9uZGhlcjcyOUBnbWFpbC5jb20iLCJyb2xlIjoibGF3eWVyIiwiZXhwIjoxNzY2MzU1NzcwfQ.yqT79e-T0_NcccNVRwg-juMDGBv6lJqNQ-NCv9eYd3E'
        },
        // body: JSON.stringify(data)
    };

    // Send POST request
    fetch('http://192.168.43.176:8001/api/lawyers/user', options)
        .then(response => response.json())
        .then(data => {
            console.log('Response:', data);
            document.getElementById('response').innerText = 'Rating submitted successfully!';
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('response').innerText = 'Error submitting rating';
        });
}
