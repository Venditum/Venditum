mal2 :: Int -> Int
mal2 x = x * 2

fakultät :: Int -> Int
fakultät 0 = 1
fakultät n = (fakultät (n - 1)) * n

fibonacci :: Int -> Int
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n - 1) + fibonacci (n - 2)

größeres :: Int -> Int -> Int
größeres a b
    | a < b = b
    | otherwise = a

erstes :: (Eq a) => [a] -> a
erstes [] = error ("Liste leer!")
erstes (x:xs) = x

letztes :: [a] -> a
letztes [] = error ("Liste leer!")
letztes [x] = x
letztes (x:xs) = letztes xs

summe :: [Int] -> Int
summe [] = -1
summe [x] = x
summe (x:xs) = x + summe xs

länge :: [a] -> Int
länge [] = 0
länge [x] = 1
länge (x:xs) = länge xs + 1

länges :: [Int] -> Int
länges [] = 0
länges (x:xs) = (ceiling (fromIntegral (länge (x:xs)) / 2))

nimm :: Int -> [a] -> a
nimm n [] = error ("Liste leer!")
nimm 1 (x:xs) = x
nimm n (x:xs) 
    | n > (länge (x:xs)) = error ("Liste leer!")
    | otherwise = nimm (n - 1) xs

maxi :: [Int] -> Int
maxi [] = error ("Liste leer!")
maxi [x] = x
maxi (x:y:ys)
    | x > y = maxi (x:ys)
    | otherwise = maxi (y:ys)

enthalten :: [Int] -> Int -> Bool
enthalten [] n = False
enthalten (x:xs) n
    | n == x = True
    | otherwise = enthalten xs n

entfernen :: [Int] -> Int -> [Int]
entfernen [] _ = error ("Liste leer!")
entfernen (x:xs) n
    | n == x = xs
    | otherwise = entfernen xs (n - 1)

e :: [a] -> [a]
e [] = error ("Liste leer!")
e (x:xs) = xs

umdrehen :: [a] -> [a]
umdrehen [] = []
umdrehen (x:xs) = umdrehen xs ++ [x]

palindrom :: String -> Bool
palindrom [] = True
palindrom [x] = True
palindrom (x:xs) 
    | x == nimm (länge (x:xs)) (x:xs) = palindrom (e (umdrehen xs))
    | otherwise = False

kleinstes :: [Int] -> Int
kleinstes [] = error ("Liste kleinstes!")
kleinstes [x] = x
kleinstes (x:y:ys)
    | x < y = kleinstes (x:ys)
    | otherwise = kleinstes (y:ys)

gerade :: Int -> Bool
gerade x
    | mod x 2 == 0 = True
    | otherwise = False

prim_helper :: Int -> Int -> Bool
prim_helper x y
    | y > (x - 2) = True
    | mod x y == 0 = False
    | otherwise = prim_helper x (y + 1)

prim :: Int -> Bool
prim 2 = True
prim x 
    | x /= 1 && prim_helper x 2 == True = True
    | otherwise = False

-- sortieren :: [Int] -> [Int]    
-- sortieren [] = []
-- sortieren xs = k:sortieren (löschen xs k)
--     where k = kleinstes xs

filter_ :: (Int -> Bool) -> [Int] -> [Int]
filter_ f [] = []
filter_ f (x:xs) 
    | f x == True = x:filter_ f xs
    | otherwise = filter_ f xs

zipper :: (Int -> Int -> Int) -> [Int] -> [Int] -> [Int]
zipper f [] [] = []
zipper f (x:xs) (y:ys) = (f x y):zipper f xs ys  

folder :: (Int -> Int -> Int) -> Int -> [Int] -> Int
folder f y [] = y
folder f n [x] = f n x
folder f n (x:y:ys) = folder f n (ys ++ [f x y])

insertion :: [Int] -> Int -> [Int]
insertion [] n = [n]
insertion (x:xs) n
    | n > x = x:insertion xs n
    | otherwise = [n] ++ (x:xs)

insertionSort :: [Int] -> [Int]
insertionSort [] = []
insertionSort [x] = [x]
insertionSort (x:xs) = insertion (insertionSort xs) x

bubble :: [Int] -> [Int]
bubble [] = []
bubble [x] = [x]
bubble (x:y:ys)
    | x <= y = x:bubble (y:ys)
    | otherwise = y:bubble (x:ys)

bubbleSort :: [Int] -> [Int]
bubbleSort [] = []
bubbleSort (x:xs) = bubble (x:bubbleSort xs)

merge :: [[Int]] -> [Int]
merge [[], []] = []
merge [(x:xs), []] = (x:xs)
merge [[], (y:ys)] = (y:ys)
merge [(x:xs), (y:ys)]
    | x <= y = insertionSort (x:merge [xs, (y:ys)])
    | otherwise = insertionSort (y:merge [(x:xs), ys])

anzahlen :: [Char] -> [Int]
anzahlen [] = []
anzahlen [x] = [1]
anzahlen (x:y:ys)
    | x == y = head anzahlenTail + 1:tail anzahlenTail
    | otherwise = 1:anzahlen (y:ys)
    where anzahlenTail = anzahlen (y:ys)

packen :: [Char] -> [[Char]]
packen [] = [[]]
packen [x] = [[x]]
packen (x:y:ys)
    | x == y = (x:head packenTail):tail packenTail
    | otherwise = [x]:packenTail
    where packenTail = packen (y:ys)

lauflängenkodierung :: [Char] -> [(Int, Char)]
lauflängenkodierung [] = []
lauflängenkodierung [x] = [(1, x)]    
lauflängenkodierung (x:y:ys)
    | x == y = ((fst (head lauflängenkodierungTail)) + 1, x):tail lauflängenkodierungTail
    | otherwise = (1, x):lauflängenkodierungTail
    where lauflängenkodierungTail = lauflängenkodierung (y:ys)

lauflängendekodierung :: [(Int, Char)] -> [Char]
lauflängendekodierung [] = []
lauflängendekodierung [(1, x)] = [x] 
lauflängendekodierung (x:xs)
    | (fst x) > 1 = (snd x):lauflängendekodierung ((fst x - 1, snd x):xs)
    | otherwise = (snd x):lauflängendekodierung xs

flipper :: (a -> b -> c) -> (b -> a -> c) 
flipper f x y = f y x   