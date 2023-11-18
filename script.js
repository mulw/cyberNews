document.addEventListener('DOMContentLoaded', () => {
    const newsContainer = document.getElementById('news-container');

    // Fetch news function
    const fetchNews = async () => {
        try {
            const apiKey = '881122986ae7429ab8496abe2b929e0f';
            const response = await fetch('http://localhost:3000/news');
            const data = await response.json();

            // Clear existing content
            newsContainer.innerHTML = '';

            if (data.articles && data.articles.length > 0) {
                data.articles.forEach(article => {
                    const articleHTML = `
                        <div class="news-article">
                            <h2>${article.title}</h2>
                            <p>${article.description}</p>
                            <time>${new Date(article.publishedAt).toLocaleString()}</time>
                            <a href="${article.url}" target="_blank">Read more</a>
                        </div>
                    `;

                    // Add the HTML to the news container
                    newsContainer.innerHTML += articleHTML;
                });
            } else {
                newsContainer.innerHTML = '<p>No articles found.</p>';
            }
        } catch (error) {
            console.error('Error fetching news:', error);
            newsContainer.innerHTML = '<p>Error fetching news. Please try again later.</p>';
        }
    };

    // Fetch news on page load
    fetchNews();

    // Fetch news every 3 minutes
    setInterval(fetchNews, 180000); // Update every 3 minutes
});

