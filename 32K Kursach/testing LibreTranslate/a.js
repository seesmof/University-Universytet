a =
  "For this God is our God for ever and ever: he will be our guide even unto death. (Psalms 48:14)";

const translate = async function (a) {
  const res = await fetch("https://translate.flossboxin.org.in/translate", {
    method: "POST",
    body: JSON.stringify({
      q: a,
      source: "auto",
      target: "uk",
      format: "text",
      alternatives: 3,
      api_key: "",
    }),
    headers: { "Content-Type": "application/json" },
  });

  console.log(await res.json());
};

translate(a);
