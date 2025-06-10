const form = document.querySelector("form");
const antwortbox = document.getElementById("antwortbox");


async function rechnen(event) {
  event.preventDefault();
  const formData = new FormData(form);
  try {
    const query = new URLSearchParams(formData).toString();
    const res = await fetch("/rechnen?" + query)
    console.log(`Hallo ich bin ${query}`)
    const data = await res.json()
    if (data.error) {
      antwortbox.innerHTML = `<p style="color: red;">${data.error}</p>`;
    }
    else {
      antwortbox.innerHTML = `<p style="color: green;">${data.antwort}</p>
          ${data.rechnung ? `<p><strong>${data.rechnung}</strong></p>` : ""}
        `;
      form.reset();
    }
  }
  catch (err) {
    antwortbox.innerHTML = "<p style='color: red;'>⚠️Ups, hier ist was schiefgelaufen.</p>";
  }

}
form.addEventListener("submit", rechnen)