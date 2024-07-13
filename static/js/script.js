function searchBrands() {
    const brands = document.getElementById('brand-input').value;
    const keyword = document.getElementById('keyword-input').value;
    const progressBar = document.getElementById('progress-bar');

    document.getElementById('loading').style.display = 'block';
    progressBar.style.width = '0%';
    document.getElementById('download-button').style.display = 'none';

    // Start the progress bar
    const eventSource = new EventSource('/progress');
    eventSource.onmessage = function(event) {
        const progress = event.data;
        progressBar.style.width = progress + '%';
        if (progress >= 100) {
            eventSource.close();
        }
    };

    fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'brands=' + encodeURIComponent(brands) + '&keyword=' + encodeURIComponent(keyword),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('loading').style.display = 'none';

        const tableBody = document.getElementById('results-table').getElementsByTagName('tbody')[0];
        tableBody.innerHTML = '';
        data.results.forEach(row => {
            const newRow = tableBody.insertRow();
            const cell1 = newRow.insertCell(0);
            const cell2 = newRow.insertCell(1);
            cell1.textContent = row.Brand;
            cell2.textContent = row.Website;
        });

        document.getElementById('download-button').setAttribute('data-filename', data.filename);
        document.getElementById('download-button').style.display = 'block';
    })
    .catch(error => console.error('Error:', error));
}

function downloadCSV() {
    const filename = document.getElementById('download-button').getAttribute('data-filename');
    window.location.href = '/download/' + filename;
}
