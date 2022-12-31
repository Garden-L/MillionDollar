//middleware
mw = {};
module.exports = mw;

mw.isLoggedIn = (req, res, next) =>{
    if (req.isAuthenticated()){
        next();
    } else {
        res.redirect('/login');
    }
};

mw.isNotLoggedIn = (req, res, next) =>{
    if (!req.isAuthenticated()){
        next();
    } else {
        const message = encodeURIComponent('로그인한 상태입니다');
        res.redirect(`/?error=${message}`);
    }
}