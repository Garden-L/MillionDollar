const express = require('express');
const path = require('path');
const morgan = require('morgan');
const nunjucks = require('nunjucks');
const session = require('express-session');
const dotenv = require('dotenv');
const cookieParser = require('cookie-parser');
const SessionStore = require('express-session-sequelize')(session.Store);

const passport = require('passport');
const passportConfig = require('./passport');

const { sequelize } = require('./models');
const rootRouter = require('./routes/root');

const app = express();

dotenv.config();
app.set('port', process.env.PORT || 3000);
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
    SaveUninitialized: false,
    secret: process.env.COOKIE_SECRET,
    cookie: {
        httpOnly: true,
        secure: false,
    },
}));
passportConfig();
app.use(passport.initialize());
app.use(passport.session());

app.use('/', rootRouter);

app.use((req, res, next) => {
    const error = new Error(`${req.method} ${req.url} 라우터가 없습니다.`);
    error.status = 404;
    next(error);
});

app.use((err, req, res, next) => {
    res.locals.message = err.message;
    res.locals.error = process.env.NODE_ENV !== 'production' ? err: {};
    res.status(err.status || 500);
    res.render('404.html');
});

app.listen(app.get('port'), () => {
    console.log(app.get('port'), '번 포트에서 대기 중');
});

