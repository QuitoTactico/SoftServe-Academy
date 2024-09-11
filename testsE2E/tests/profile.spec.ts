import { test } from '@playwright/test';

test.beforeEach(async ({ page }) => {
    await page.goto('http://127.0.0.1:8000/');
    await page.getByRole('link', { name: 'Login' }).click();
    await page.getByLabel('Email:').click();
    await page.getByLabel('Email:').fill('teteban0917@gmail.com');
    await page.getByLabel('Password:').click();
    await page.getByLabel('Password:').fill('Teteban0917');
    await page.getByRole('button', { name: 'Login' }).click();
});

test.describe('profileSetup', () => {

    test('learning preferences', async ({ page }) => {
        await page.getByRole('link', { name: 'Learning Preferences' }).click();

        const MEDIA_TYPES = ['Video', 'Audio', 'Text'];
        await page.getByLabel('Media type:').selectOption(MEDIA_TYPES[Math.floor(Math.random() * MEDIA_TYPES.length)]);

        const CONTENT_TYPES = ['Guides', 'Documentation', 'Introduction', 'Summary', 'Article', 'Quiz', 'Podcast'];
        await page.getByLabel('Content type:').selectOption(CONTENT_TYPES[Math.floor(Math.random() * CONTENT_TYPES.length)]);

        const LEARNIGN_TYPE = ['Autodidact', 'Guided', 'Challenges'];
        await page.getByLabel('Learning type:').selectOption(LEARNIGN_TYPE[Math.floor(Math.random() * LEARNIGN_TYPE.length)]);

        await page.getByLabel('Time per Week (Minutes):').click();
        await page.getByLabel('Time per Week (Minutes):').fill(Math.floor(Math.random() * 600).toString());

        await page.getByLabel('Time per Session (Minutes):').click();
        await page.getByLabel('Time per Session (Minutes):').fill(Math.floor(Math.random() * 600).toString());

        await page.getByRole('button', { name: 'Save Preferences' }).click();
    });

    test('update info', async ({ page }) => {
        await page.getByRole('link', { name: 'Account Info' }).click();
        await page.getByPlaceholder('Enter your name').click();
        await page.getByPlaceholder('Enter your name').fill('sdfasdf');
        await page.getByRole('button', { name: 'Update Profile' }).click();
    });

    test('current skill', async ({ page }) => {
        await page.getByRole('link', { name: 'Current Skills', exact: true }).click();
        await page.getByLabel('Current Skills:').selectOption(['1', '2', '4', '10', '13', '14', '20']);
        await page.getByRole('button', { name: 'Update Current Skills' }).click();
    });

    test('target skill', async ({ page }) => {
        await page.getByRole('link', { name: 'Target Skills' }).click();
        await page.getByLabel('Target Skills:').selectOption(['6', '7', '10', '15', '18']);
        await page.getByRole('button', { name: 'Update Target Skills' }).click();
    });
    
});