import { test } from '@playwright/test';

test.beforeEach(async ({ page }) => {
    await page.goto('http://127.0.0.1:8000/');
});

test.describe('User singup/login', () => {

    test('signup', async ({ page }) => {
        await page.getByRole('banner').getByRole('link', { name: 'Get Started' }).click();
        await page.getByLabel('Name:').click();
        await page.getByLabel('Name:').fill('user1');
        await page.getByLabel('Email:').click();
        await page.getByLabel('Email:').fill('user1@email.com');
        await page.getByLabel('Password:', { exact: true }).click();
        await page.getByLabel('Password:', { exact: true }).fill('12345');
        await page.getByLabel('Confirm password:').click();
        await page.getByLabel('Confirm password:').fill('12345');
        await page.getByRole('button', { name: 'Register' }).click();
    });

    test('login', async ({ page }) => {
        await page.getByRole('link', { name: 'Login' }).click();
        await page.getByLabel('Email:').click();
        await page.getByLabel('Email:').fill('user1@email.com');
        await page.getByLabel('Password:').click();
        await page.getByLabel('Password:').fill('12345');
        await page.getByRole('button', { name: 'Login' }).click();
    });

});