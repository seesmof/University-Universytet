async function loadText(reference) {
    const baseUrl = 'https://open-bible-api.vercel.app/'
    const response = await fetch(`${baseUrl}${reference}`)
    const data = await response.json();
    return data
}

const reference = '1JN/1/1';
const response = loadText(reference);
console.log(response);