async function generateComic() {
    // Collect text inputs from the form
    const inputs = [];
    for (let panel = 1; panel <= 10; panel++) {
        inputs.push(document.getElementById(`panel${panel}`).value);
    }

    // Make API call
    fetch('/generate_comic', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ inputs: inputs })
    })
    .then(response => response.json())
    .then(data => {
        // Display the generated comic
        const comicDisplay = document.getElementById('comicDisplay');
        comicDisplay.innerHTML = '';
        data.forEach(imageSrc => {
            const img = document.createElement('img');
            img.src = 'data:image/png;base64,' + imageSrc;
            comicDisplay.appendChild(img);
        });
    })
    .catch(error => {
        console.error('Error:', error);
        // Provide user feedback for errors
        alert('Failed to generate comic. Please try again.');
    });
}
