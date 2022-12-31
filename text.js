const express = require('express');
const path = require('path');
const morgan = require('morgan');
const nunjucks = require('nunjucks');
const session = require('express-session');
const dotenv = require('dotenv');
const cookieParser = require('cookie-parser');
const passport = require('passport');

const { sequelize } = require('./models');
const { router }    = require('./routes/routers')

const app = express();

dotenv.config();
app.set('port', process.env.PORT || 4000);
app.set('view engine', 'html');
nunjucks.configure('views', {
    express: app,
    watch: true,
});

app.use(morgan('dev'));
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.urlencoded({extended: false}));
app.use(express.json());
app.use(cookieParser(process.env.COOKIE_SECRET));
app.use(session({
    resave: false,
    saveUninitialized: false,
    secret: process.env.COOKIE_SECRET,
    cookie: {
        httpOnly: true,
        secure: false, 
    },
}));
passport.serializeUser((user, done) =>{
    done(null, user.id);
    console.log('fwfw');
});

passport.serializeUser((user, done) =>{
    done(null, user.id);
    console.log('fwfw');
});
passport.deserializeUser((id, done)=>{
    done(null, id);
});
passport.fewfwef = ()=>{console.log("ewfwe")};

app.get('/', (req, res) => {
    console.log(req);
    passport.login();
})

app.listen(app.get('port'), () => {
    console.log(app.get('port'), '번 포트에서 대기 중');
});

