CREATE TABLE "user" (
  "id" SERIAL CONSTRAINT "pk_user" PRIMARY KEY,
  "name" TEXT NOT NULL,
  "email" TEXT NOT NULL UNIQUE,
  "password" TEXT NOT NULL
);

CREATE TABLE "category" (
  "id" SERIAL CONSTRAINT "pk_category" PRIMARY KEY,
  "name" TEXT NOT NULL UNIQUE,
  "label" TEXT NOT NULL,
  "user" INTEGER NOT NULL

);

CREATE INDEX "idx_category__user" ON "category" ("user");

ALTER TABLE "category" ADD CONSTRAINT "fk_category__user" FOREIGN KEY ("user") REFERENCES "user" ("id");

CREATE TABLE "expense" (
  "id" SERIAL CONSTRAINT "pk_expense" PRIMARY KEY,
  "name" TEXT NOT NULL,
  "amount" DOUBLE PRECISION,
  "date" TIMESTAMP,
  "user" INTEGER NOT NULL,
  "category" INTEGER NOT NULL
);

CREATE INDEX "idx_expense__category" ON "expense" ("category");

CREATE INDEX "idx_expense__user" ON "expense" ("user");

ALTER TABLE "expense" ADD CONSTRAINT "fk_expense__category" FOREIGN KEY ("category") REFERENCES "category" ("id");

ALTER TABLE "expense" ADD CONSTRAINT "fk_expense__user" FOREIGN KEY ("user") REFERENCES "user" ("id")