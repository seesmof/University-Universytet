const fetchData = async (url) => {
  const response = await fetch(url);
  const data = await response.json();
  return data;
};

const renderData = (data, BookNumber, chapterNumber) => {
  const fragment = document.createDocumentFragment();

  data.forEach((element) => {
    const verseNumber = document.createElement("span");
    verseNumber.innerText = element.verse;
    verseNumber.style.fontWeight = "bold";
    const combinedElement = document.createElement("span");
    if (element.verse !== 1) {
      verseNumber.style.verticalAlign = "super";
      verseNumber.style.fontSize = "0.7em";
      combinedElement.appendChild(document.createTextNode(" "));
    } else {
      verseNumber.innerHTML = chapterNumber;
    }

    const verseText = document.createElement("span");
    const parser = new DOMParser();
    const doc = parser.parseFromString(element.text, "text/html");
    verseText.innerHTML = doc.body.innerHTML.trim();

    combinedElement.appendChild(verseNumber);
    combinedElement.appendChild(document.createTextNode(" "));
    combinedElement.appendChild(verseText);

    fragment.appendChild(combinedElement);
  });

  fragment.appendChild(document.createTextNode(" "));
  document.getElementById("container").appendChild(fragment);
};

fetchData("https://bolls.life/get-chapter/BSB/1/1/").then((data) =>
  renderData(data, 1, 1)
);
fetchData("https://bolls.life/get-chapter/BSB/1/2/").then((data) =>
  renderData(data, 1, 2)
);
fetchData("https://bolls.life/get-chapter/BSB/1/3/").then((data) =>
  renderData(data, 1, 3)
);
