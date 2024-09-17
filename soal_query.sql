#Soal No 1
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO users (username, email, password) VALUES
('Andi', 'andi@andi.com', '12345'),
('Budi', 'budi@budi.com', '67890'),
('Caca', 'caca@caca.com', 'abcde'),
('Deni', 'deni@deni.com', 'fghij'),
('Euis', 'euis@euis.com', 'klmno'),
('Fafa', 'fafa@fafa.com', 'pqrst');
SELECT * FROM users;

#Soal NO 2
CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    course VARCHAR(50) NOT NULL,
    mentor VARCHAR(50) NOT NULL,
    title VARCHAR(50) NOT NULL
);
INSERT INTO courses (course, mentor, title) VALUES
('C++', 'Ari', 'Dr.'),
('C#', 'Ari', 'Dr.'),
('C#', 'Ari', 'Dr.'),
('CSS', 'Cania', 'S.Kom'),
('HTML', 'Cania', 'S.Kom'),
('Javascript', 'Cania', 'S.Kom'),
('Python', 'Barry', 'S.T.'),
('Micropython', 'Barry', 'S.T.'),
('Java', 'Darren', 'M.T.'),
('Ruby', 'Darren', 'M.T.');
SELECT * FROM courses;



# Soal No 3
CREATE TABLE userCourse (
    id_user INT NOT NULL,
    id_course INT NOT NULL,
    PRIMARY KEY (id_user, id_course)
);

INSERT INTO userCourse (id_user, id_course) VALUES
(1, 1), 
(1, 2), 
(1, 3),
(2, 4), 
(2, 5), 
(2, 6),
(3, 7),
(3, 8),
(3, 9),
(4, 1),
(4, 3),
(4, 5),
(5, 2),
(5, 4),
(5, 6),
(6, 7),
(6, 8),
(6, 9);

SELECT * FROM userCourse;


# Soal No 4
SELECT u.id, u.username, c.course, c.mentor, c.title 
FROM userCourse uc
JOIN users u ON uc.id_user = u.id
JOIN courses c ON uc.id_course = c.id
ORDER BY u.id;


#Soal No 5
SELECT u.id, u.username, c.course, c.mentor, c.title
FROM userCourse uc
JOIN users u ON uc.id_user = u.id
JOIN courses c ON uc.id_course = c.id
WHERE c.title LIKE 'S.%'
ORDER BY u.id;


#Soal No 6
SELECT u.id, u.username, c.course, c.mentor, c.title
FROM userCourse uc
JOIN users u ON uc.id_user = u.id
JOIN courses c ON uc.id_course = c.id
WHERE c.title NOT LIKE 'S.%'
ORDER BY u.id;


#Soal No 7
SELECT c.course, c.mentor, c.title, COUNT(uc.id_user) AS jumlah_peserta
FROM userCourse uc
JOIN courses c ON uc.id_course = c.id
GROUP BY c.course, c.mentor, c.title;

#Soal No 8
SELECT c.mentor, COUNT(uc.id_user) AS jumlah_peserta, (COUNT(uc.id_user) * 2000000) AS total_fee
FROM userCourse uc
JOIN courses c ON uc.id_course = c.id
GROUP BY c.mentor;

