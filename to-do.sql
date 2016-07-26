CREATE TABLE task (
  id serial PRIMARY KEY,
  task_description text,
  completed boolean
);

insert into task values
  (default, 'Take a break', False);
insert into task values
  (default, 'Code', False);
insert into task values
  (default, 'Apply to jobs', False);
insert into task values
  (default, 'Change careers', True);
