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

	test('add resourse', async ({ page }) => {
		await page.getByRole('link', { name: 'Admin' }).click();
		await page.getByRole('row', { name: 'Learning resources Add Change' }).getByRole('link').nth(1).click();

		await page.getByLabel('Name:').click();
		await page.getByLabel('Name:').fill('resourseX');

		const MEDIA_TYPES = ['Video', 'Audio', 'Text'];
		await page.getByLabel('Media type:').selectOption(MEDIA_TYPES[Math.floor(Math.random() * MEDIA_TYPES.length)]);

		const CONTENT_TYPES = ['Guides', 'Documentation', 'Introduction', 'Summary', 'Article', 'Quiz', 'Podcast'];
		await page.getByLabel('Content type:').selectOption(CONTENT_TYPES[Math.floor(Math.random() * CONTENT_TYPES.length)]);

		await page.getByLabel('Link:').click();
		await page.getByLabel('Link:').fill('randomvideoX');

		await page.getByLabel('Details:').click();
		await page.getByLabel('Details:').fill('lorem ipsum');

		await page.getByLabel('Duration:').click();
		await page.getByLabel('Duration:').fill('123');

		const LANGUAJES = ['en', 'es', 'pt', 'zh', 'hi', 'ja']
		await page.getByLabel('Language:').selectOption(LANGUAJES[Math.floor(Math.random() * LANGUAJES.length)]);

		await page.getByLabel('Original platform:').click();
		await page.getByLabel('Original platform:').fill('somewhere');

		await page.getByLabel('Original author:').click();
		await page.getByLabel('Original author:').fill('someone');

		await page.getByLabel('General level:').click();
		await page.getByLabel('General level:').fill(Math.ceil(1 + Math.random() * 4).toString());

		await page.getByLabel('Learning skills:').selectOption(Math.floor(1 + Math.random() * 10).toString());
		await page.getByLabel('Required skills:').selectOption(Math.floor(1 + Math.random() * 10).toString());
		await page.getByRole('button', { name: 'Save', exact: true }).click();
	});
});