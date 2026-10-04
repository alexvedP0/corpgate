const puppeteer = require('puppeteer-core');
(async () => {
    const browser = await puppeteer.launch({
        executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        headless: 'new'
    });
    const page = await browser.newPage();
    await page.setViewport({ width: 1920, height: 1080 });
    await page.goto('https://corpgate.vercel.app/www.corpgate.com/index.html', { waitUntil: 'networkidle2' });
    await page.screenshot({ path: 'local_screenshot.png' });
    await browser.close();
    console.log('Screenshot saved!');
})();
