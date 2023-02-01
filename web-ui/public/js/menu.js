

const loader = document.getElementById("loader");
const content = document.getElementById("content");

function loading(){
    loader.hidden = false;
    content.hidden = true;
}


function complete(){
    loader.hidden = true;
    content.hidden = false;
}

function sleep(ms) {
    return new Promise(
      resolve => setTimeout(resolve, ms)
    );
  }

async function getMenu(){
    try{
         loading();
         const apiUrl = await fetch("http://127.0.0.1:8000/menu");
         const response = await apiUrl.json();
         response.map((menu) => {
              const div = document.createElement("div");
              div.textContent = menu.name;
              content.appendChild(div);
         });

         await sleep(2000);
         complete();

    }catch(error){
        console.log(error)
    }
}

getMenu();