import { test } from '@playwright/test';

test.beforeEach(async ({ page }) => {
    await page.goto('http://127.0.0.1:8000/');
    await page.getByRole('link', { name: 'Login' }).click();
    await page.getByLabel('Email:').click();
    await page.getByLabel('Email:').fill('user1@email.com');
    await page.getByLabel('Password:').click();
    await page.getByLabel('Password:').fill('12345');
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

        await page.getByLabel('Time per week:').click();
        await page.getByLabel('Time per week:').fill(Math.floor(Math.random() * 10).toString());

        await page.getByLabel('Time per session:').click();
        await page.getByLabel('Time per session:').fill(Math.floor(Math.random() * 10).toString());

        await page.getByRole('button', { name: 'Save Preferences' }).click();
    });

    test('current skill', async ({ page }) => {

    });

    test('target skill', async ({ page }) => {

    });

});