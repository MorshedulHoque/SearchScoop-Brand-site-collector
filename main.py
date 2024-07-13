from flask import Flask, render_template, request, jsonify, send_file, Response
import pandas as pd
from googlesearch import search
import time

app = Flask(__name__)

progress = 0

# Function to perform Google search and extract website
def get_website_from_google(query):
    try:
        search_results = search(query, num_results=1)
        for result in search_results:
            return result
    except Exception as e:
        print(f"Error: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_brands():
    global progress
    brand_names = request.form['brands'].split('\n')
    keyword = request.form['keyword']
    results = []
    total_brands = len(brand_names)

    progress = 0
    for i, brand in enumerate(brand_names):
        query = f"{brand} {keyword}"
        website = get_website_from_google(query)
        results.append({'Brand': brand, 'Website': website})
        progress = (i + 1) / total_brands * 100
        time.sleep(1)  # Simulating processing time

    # Save results to CSV with a Unix timestamp
    timestamp = int(time.time())
    filename = f'output_file_{timestamp}.csv'
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)

    return jsonify({'results': results, 'filename': filename})

@app.route('/progress')
def progress_stream():
    def generate():
        global progress
        while progress < 100:
            yield f"data:{progress}\n\n"
            time.sleep(1)
        yield "data:100\n\n"  # Ensure the progress ends at 100%
    return Response(generate(), mimetype='text/event-stream')

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
