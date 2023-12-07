import { Config } from 'drizzle-kit'

import 'dotenv/config'; // see https://github.com/motdotla/dotenv#how-do-i-use-dotenv-with-import

export default {
    schema: "./src/db/schema.ts",
    driver: 'pg',
    dbCredentials: {
        connectionString: process.env.DB_URL ?? '',
    },
    verbose: true,
    strict: true,
} satisfies Config