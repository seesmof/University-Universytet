const fetchData = async (url) => {
  const response = await fetch(url);
  const data = await response.json();
  return data;
};

fetchData("https://bolls.life/get-chapter/UTT/22/8/").then((data) =>
  console.log(data)
);
