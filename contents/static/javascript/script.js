function postFormData(relativeApiLink) {
    const absoluteApiLink = window.location.origin + relativeApiLink;

    const form = document.querySelector('#my-form');

    const imageContainer = document.querySelector('#image-container');

    form.addEventListener('submit', async (event) => {
      event.preventDefault();

      const formData = new FormData(form);
  
      if (!formData.get('file')) {
        alert('Please select a file to upload.');
        return;
      }
      imageContainer.innerHTML = 'Loading...';

      const response = await fetch(absoluteApiLink, {
        method: 'POST',
        body: formData
      });
      if (response.ok) {
        const responseData = await response.json();
        if (responseData.error) {
            
          imageContainer.innerHTML = resp
        } else {
          const imageUrls = responseData.url;

          const imageHtml = imageUrls.map(url => '<img class="from-api" src="${url}" alt="Image">').join('');

          imageContainer.innerHTML = imageHtml;
        }
      } else {
        imageContainer.innerHTML = "<p class='error'>Error: ${response.status}</p>";
      }
    });
  }
