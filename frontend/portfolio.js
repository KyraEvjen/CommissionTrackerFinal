let nameInput = document.getElementById('name');
let descrInput = document.getElementById('description');
let portfolios = document.getElementById('portfolios'); 
let portfolioId = document.getElementById('portfolio-id');

let imgString = '';
let data = [];

const api = 'http://127.0.0.1:8000';
//used for getting the image
function previewFiles() 
    {
    const preview = document.querySelector("#preview");
    const files = document.querySelector("input[type=file]").files;

    function readAndPreview(file) {
        const reader = new FileReader();
        reader.addEventListener(
          "load",
          () => {
            const image = new Image();
            image.height = 100;
            image.title = file.name;
            image.src = reader.result;
            preview.appendChild(image);
            //console.log(image.src);
            imgString = image.src;
          },
          false,
        );
        reader.readAsDataURL(file);
        //console.log(file);
    }
    if (files) {
      Array.prototype.forEach.call(files, readAndPreview);
    }
  }


function tryAdd() {
    let msg = document.getElementById('msg');
    const preview = document.querySelector("#preview");
    preview.innerHTML = '';
    msg.innerHTML = '';
  }

  //MONGODB THINGS
// Function to fetch portys from the backend
async function getPortfolios() {
    try {
      const response = await fetch(`${api}/portfolios`);
      if (!response.ok) {
        throw new Error('Failed to fetch portfolios');
      }
      const portfolios = await response.json();

      data = portfolios.portfolios;

      refreshPortfolios();
    } catch (error) {
      console.error('Error fetching portfolios:', error);
    }
  }

document.getElementById('form-add').addEventListener('submit', async (e) => {
    e.preventDefault();

    if(imgString === '')
    {
        document.getElementById('msg').innerHTML = "Must add an image";
    }
     else {

      const portfolioData = {
        name: nameInput.value,
        image: imgString,
        description: descrInput.value
      };
        const response = await fetch(`${api}/portfolios`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(portfolioData)
        });
        refreshPortfolios();
        if (!response.ok) {
          throw new Error('Failed to add portfolio');
        }
  
        //addCommission(commissionData);
        refreshPortfolios();
  
        // Close Modal
        let add = document.getElementById('add');
        add.setAttribute('data-bs-dismiss', 'modal');
        add.click();
        (() => {
          add.setAttribute('data-bs-dismiss', '');
        })();
  
        // Reset the Text and Progress Bar
        preview = document.querySelector("#preview");
        preview.innerHTML = '';
        msg = document.getElementById('msg');
        msg.innerHTML = '';
        getPortfolios();
        refreshPortfolios();
      } 
  });


  
  // Function to refresh portys on the UI
  function refreshPortfolios() {
  
    portfolios.innerHTML = '';
    Array.from(data).forEach((x) => {
      portfolios.innerHTML += `
      <div class = "responsive">
      <div class="gallery">
            <div id="portfolio-${x._id}">
            <img src =${x.image} width = "200">
            <div class = "description">${x.description}</div>
            <pre class="fw-bold fs-4">${x.name}</pre>

                <i onClick="tryEditPortfolio('${x._id}')" data-bs-toggle="modal" data-bs-target="#modal-edit" class="fas fa-edit"></i>
                <i onClick="deletePortfolio('${x._id}')" class="fas fa-trash-alt"></i>
            
            </div>
        </div>    
        </div>
      `;
    });
    resetForm();
  }

  async function tryEditPortfolio(id) {
    // Find the commission with the specified ID
    const portfolio = data.find(obj => obj._id === id);
  
    // Populate the modal with the commission details
    document.getElementById('name-edit').value = portfolio.name;
    document.getElementById('description-edit').value = portfolio.description;
    document.getElementById('image-edit').value = portfolio.image;
    document.getElementById('portfolio-id').textContent = id;
  }
  
    // Add event listener for the form submission
  const formEdit = document.getElementById('form-edit');
    formEdit.addEventListener('submit', async (event) => {
    event.preventDefault();
  
    const updatedPortfolio = {
        name: document.getElementById('name-edit').value,
        description: document.getElementById('description-edit').value,
        image: document.getElementById('image-edit').value,
    };

    const id = document.getElementById('portfolio-id').textContent;
  
    try {
        // Send a PUT request to update the port in the database
        const response = await fetch(`${api}/portfolios/${id}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(updatedPortfolio),
      });      

  
      if (!response.ok) {
          throw new Error('Failed to update portfolio');
      }
        
      getPortfolios();
      refreshPortfolios();
  
      } catch (error) {
        console.error('Error updating portfolio:', error);
        // Handle error
      }
    });

  function editPorfolio(id){
    tryEditPortfolio(id);
  }

  function resetForm() {
    nameInput.value = '';
    descrInput.value = '';
    imgString = ''
    preview = document.querySelector("#preview");
    preview.innerHTML = '';
    msg = document.getElementById('msg');
    msg.innerHTML = '';
  }
getPortfolios();

  async function deletePortfolio(id) {

    try {
      const response = await fetch(`${api}/portfolios/${id}`, {
        method: 'DELETE',
      });
      if (!response.ok) {
        throw new Error('Failed to delete portfolio');
      }
      data = data.filter((x) => x._id !== id);
      refreshPortfolios();
    } catch (error) {
      console.error('Error deleting portfolios:', error);
    }
  }
