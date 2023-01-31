import express from 'express';
import workingHours from './data/workingHours.js';
import menuItems from './data/menuItems.js';

const app = express();

if(!process.env.PORT){
    throw new Error("Impossible de lancer l'application. Veillez fournir le numéro de port via la variable d'environnement PORT s'il vous plaît");
}


const port = process.env.PORT;


app.use(express.static("public"));


app.set("view engine", "ejs");


app.get("/", (req, res) => {
    res.render("index", { name: "Welcome to What Fare is Fair!" });
});


app.get("/menu", (req, res) => {
    res.render("menu", { menuItems });
});


app.get("/about", (req, res) => {
    res.json({"message": "Welcome to the app"})
});


// app.get("/hours", (req, res) => {
    //     res.render("hours", { workingHours });
    // });

    
app.get('/hours', (req, res) => {
    const days = [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
        ];
        res.render("hours", { workingHours, days });
    });
    
    
app.listen(port, () => {
        console.log(`Web server is listening at localhost:${port}`);
    })
