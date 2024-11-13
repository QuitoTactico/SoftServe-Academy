import { test } from '@playwright/test';

test.beforeEach(async ({ page }) => {
    await page.goto('http://127.0.0.1:8000/');
    await page.getByRole('link', { name: 'Login' }).click();
    await page.getByLabel('Email:').click();
    await page.getByLabel('Email:').fill('mouredev@gmail.com');
    await page.getByLabel('Password:').click();
    await page.getByLabel('Password:').fill('1234');
    await page.getByRole('button', { name: 'Login' }).click();
});

test.describe('learning route', () => {

    test('create a python learning route', async ({ page }) => {
        await page.getByRole('link', { name: 'Learning Preferences' }).click();
        await page.getByLabel('Media type:').selectOption('Text');
        await page.getByLabel('Content type:').selectOption('Documentation');
        await page.getByLabel('Learning type:').selectOption('Autodidact');
        await page.getByLabel('Time per Week (Minutes):').click();
        await page.getByLabel('Time per Week (Minutes):').fill('600');
        await page.getByLabel('Time per Session (Minutes):').click();
        await page.getByLabel('Time per Session (Minutes):').fill('600');
        await page.getByRole('button', { name: 'Update Preferences' }).click();

        await page.getByRole('link', { name: 'Target Skills ' }).click();
        await page.getByRole('combobox').getByRole('list').click();
        await page.getByRole('option', { name: 'Python - 5' }).click();
        await page.getByRole('combobox').getByRole('list').click();
        await page.getByRole('option', { name: 'C++ - 5' }).click();
        await page.getByRole('button', { name: 'Update Target Skills' }).click();

        await page.getByRole('button', { name: 'Go to your learning route' }).click();
        await page.getByRole('button', { name: 'Generate Learning Routes' }).click();
        await page.getByRole('link', { name: 'Card Image Python Level' }).click();
        const page1Promise = page.waitForEvent('popup');
        await page.getByRole('link', { name: 'Python Introduction' }).click();
        const page1 = await page1Promise;
        const page2Promise = page1.waitForEvent('popup');
        await page1.getByRole('button', { name: 'Open Content' }).click();
        const page2 = await page2Promise;
    });

});