import { drizzle } from 'drizzle-orm/postgres-js';
import postgres from 'postgres';

import 'dotenv/config'; // see https://github.com/motdotla/dotenv#how-do-i-use-dotenv-with-import

const DB_URL = process.env.DB_URL;

if(!DB_URL) {
    throw new Error('DB_URL is not defined');
}

const queryClient = postgres(process.env.DB_URL!);
const db = drizzle(queryClient);

export { db };
