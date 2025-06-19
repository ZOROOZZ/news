fetch('../data/news.json') // adjust path based on your structure
  .then(response => response.json())
  .then(data => {
    const container = document.getElementById('news-container');
    data.forEach(news => {
      const card = document.createElement('div');
      card.className = 'card';
      card.innerHTML = `
        <h2>${news.title}</h2>
        <p>${news.description}</p>
      `;
      container.appendChild(card);
    });
  })
  .catch(err => console.error('Failed to load news:', err));
