const express = require('express');
const router = express.Router();
const pageRouter = require('./page');
const apiRouter = require('./api');
const authRouter = require('./auth');

router.use('/',pageRouter);
router.use('/auth', authRouter);
router.use('/api', apiRouter);

module.exports = router;