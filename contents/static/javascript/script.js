function postFormData(relativeApiLink) {
  const absoluteApiLink = window.location.origin + relativeApiLink;

  const form = document.querySelector('#my-form');

  const imageContainer = document.querySelector('#image-container');

  form.addEventListener('submit', (event) => {
    event.preventDefault();

    const formData = new FormData(form);

    // Check if all input fields have values
    let allFieldsHaveValues = true;
    const inputFields = form.querySelectorAll('input');
    inputFields.forEach(input => {
      if (!formData.get(input.name)) {

        allFieldsHaveValues = false;
      }
    });

  /*
    if (!allFieldsHaveValues) {
      alert('Please fill in all the fields.');
      return;
    }
    if (!formData.get('file')) {
      alert('Please select a file to upload.');
      return;
    }
    */

    imageContainer.innerHTML = '<div class="loader-multicolor"></div>';

    const response = fetch(absoluteApiLink, {
      method: 'POST',
      body: formData
    });

    response.then(response => {
      if (response.ok) {
        const responseData = response.json();
        responseData.then(responseData => {
          if (responseData.error) {
            imageContainer.innerHTML = `<p class='error'>${responseData.error}</p>`;
          } else {
            const imageUrls = responseData.url;

            const imageHtml = imageUrls.map(url => `<img class="from-api" src="${url}" alt="Image"></img>`).join('');

            imageContainer.innerHTML = imageHtml;
          }
        });
      } else {
        const responseData = response.json();
        responseData.then(responseData => {
          imageContainer.innerHTML = `<p class='error'>${responseData.error} </p>`;
        });
      }
    });
  });
  return;
}

function openNav() {
  document.getElementById("myNav")
  .style.height="100%";
 }


 function closeNav() {
  document.getElementById("myNav")
  .style.height = "0%";
 }
