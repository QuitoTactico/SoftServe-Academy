import { test, expect } from '@playwright/test';

test.beforeEach(async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/');
  await page.getByRole('link', { name: 'Login' }).click();
  await page.getByLabel('Email:').click();
  await page.getByLabel('Email:').fill('teteban0917@gmail.com');
  await page.getByLabel('Password:').click();
  await page.getByLabel('Password:').fill('Teteban0917');
  await page.getByRole('button', { name: 'Login' }).click();
});

test.describe('Admin tests', () => {
  
  test('create skill', async ({ page }) => {
    await page.getByRole('link', { name: 'Admin' }).click();
    await page.getByRole('row', { name: 'Skills Add Change' }).getByRole('link').nth(1).click();
    await page.getByLabel('Name:').click();
    await page.getByLabel('Name:').fill('something');
    await page.getByLabel('Skill type:').selectOption('Programming Language');
    await page.getByLabel('Name:').click();
    await page.getByLabel('Name:').press('CapsLock');
    await page.getByLabel('Name:').fill('somethingX');
    await page.getByRole('button', { name: 'Save', exact: true }).click();
  });
});