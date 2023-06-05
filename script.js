// Google Custom Search API
const apiKey = 'AIzaSyAwydGicPoEr05z1a1b6W06V2Wzl-_NVxo';
const searchEngineId = '718cd7b701a714611';
const searchInput = document.getElementById('search-input');
const searchResults = document.getElementById('search-results');

searchInput.addEventListener('keydown', async (event) => {
  if (event.key === 'Enter') {
    const query = searchInput.value;
    const url = `https://www.googleapis.com/customsearch/v1?key=${apiKey}&cx=${searchEngineId}&q=${query}`;

    try {
      const response = await fetch(url);
      const data = await response.json();
      const items = data.items;

      searchResults.innerHTML = '';

      for (const item of items) {
        const title = item.title;
        const link = item.link;
        const snippet = item.snippet;

        const resultDiv = document.createElement('div');
        resultDiv.innerHTML = `<h3><a href="${link}">${title}</a></h3><p>${snippet}</p>`;
        searchResults.appendChild(resultDiv);
      }
    } catch (err) {
      console.error(err);
      searchResults.innerHTML = '<p>There was an error retrieving search results. Please try again later.</p>';
    }
  }
});

// DeepAI API
const chatOutput = document.getElementById('chat-output');
const userInput = document.getElementById('user-input');
const deepaiApiKey = '9b3ba361-5ed2-466b-a831-5f9a722bc612';

async function generateChatbotResponse(inputText) {
  try {
    const model = await use.load();
    const embeddings = await model.embed([inputText]);
    const response = await deepai.callStandardApi('text-generator', { prompt: embeddings.arraySync() }, deepaiApiKey);
    const generatedText = response.output;

    chatOutput.innerHTML = `<p>${generatedText}</p>`;
  } catch (err) {
    console.error(err);
    chatOutput.innerHTML = '<p>There was an error generating the chatbot response. Please try again later.</p>';
  }
}

document.getElementById('chat-form').addEventListener('submit', async (event) => {
  event.preventDefault();

  const inputText = userInput.value;
  await generateChatbotResponse(inputText);

  userInput.value = '';
});

