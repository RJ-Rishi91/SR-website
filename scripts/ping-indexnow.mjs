import https from 'node:https';

const host = 'studioravya.onerishi.in';
const key = '45a8df25ec1445b98cb15d6c8b9d3e8a';
const keyLocation = `https://${host}/${key}.txt`;

const urlList = [
  `https://${host}/`,
  `https://${host}/services/`,
  `https://${host}/services/website-design-development/`,
  `https://${host}/services/landing-pages/`,
  `https://${host}/services/ecommerce-websites/`,
  `https://${host}/services/brand-and-web-identity/`,
  `https://${host}/services/custom-web-apps/`,
  `https://${host}/work/`,
  `https://${host}/work/vesper-ai/`,
  `https://${host}/work/aura-living/`,
  `https://${host}/work/monolith-protocol/`,
  `https://${host}/work/lumina-architecture/`,
  `https://${host}/work/kinetix-launch/`,
  `https://${host}/process/`,
  `https://${host}/pricing/`,
  `https://${host}/about/`,
  `https://${host}/blog/`,
  `https://${host}/blog/how-much-does-a-website-cost/`,
  `https://${host}/blog/performance-budget-core-web-vitals/`,
  `https://${host}/blog/conversion-design-principles/`,
  `https://${host}/blog/editorial-typography-guide/`,
  `https://${host}/blog/ecommerce-checkout-friction/`,
  `https://${host}/blog/rebranding-without-traffic-loss/`,
  `https://${host}/blog/why-headless-architecture-wins/`,
  `https://${host}/blog/design-tokens-and-systems/`,
  `https://${host}/blog/ai-assisted-web-development/`,
  `https://${host}/contact/`,
  `https://${host}/faq/`,
  `https://${host}/privacy-policy/`,
  `https://${host}/terms-of-service/`
];

const payload = JSON.stringify({
  host,
  key,
  keyLocation,
  urlList
});

const options = {
  hostname: 'api.indexnow.org',
  port: 443,
  path: '/IndexNow',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json; charset=utf-8',
    'Content-Length': Buffer.byteLength(payload)
  }
};

const req = https.request(options, (res) => {
  console.log(`IndexNow response status: ${res.statusCode} (${res.statusMessage})`);
  let data = '';
  res.on('data', (chunk) => { data += chunk; });
  res.on('end', () => {
    if (res.statusCode === 200 || res.statusCode === 202) {
      console.log(`Successfully submitted ${urlList.length} URLs to IndexNow! Search engines are crawling immediately.`);
    } else {
      console.log(`IndexNow response: ${data}`);
    }
  });
});

req.on('error', (e) => {
  console.error(`IndexNow error: ${e.message}`);
});

req.write(payload);
req.end();
