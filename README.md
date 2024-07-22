Για την συγκεκριμένη εργασία ζητείται να υλοποιηθεί το γνωστό σε όλους μας παιχνίδι Τρίλιζα 
με χρήση του αλγορίθμου MiniMax. O αλγόριθμος  Minimax μπορεί να θεωρηθεί ως 
αλγόριθμος τεχνητής νοημοσύνης, ο οποίος αν εφαρμοστεί σωστά δεν μπορεί σε καμία 
περίπτωση να νικηθεί από τον χρήστη στο παιχνίδι της Τρίλιζας. Συνεπώς θα υπάρχουν 2 πιθανά 
αποτελέσματα: ο υπολογιστής θα κερδίζει ή θα προκύπτει ισοπαλία αν ο χρήστης κάνει τις 
βέλτιστες κινήσεις. Ο αλγόριθμος MiniMax μπορεί να οριστεί ως μια αναδρομική 
συνάρτηση(recursive function) που κάνει κυρίως τα ακόλουθα: 
1) Επιστρέφει μια τιμή αν βρεθεί μια τελική κατάσταση. 
Μια τελική κατάσταση ορίζεται ως νίκη, ήττα ή ισοπαλία με τιμές 1, -1 , 0      
αντίστοιχα 
2) Ελέγχει όλες τις διαθέσιμες θέσεις στον πίνακα του παιχνιδιού 
3) Καλεί την συνάρτηση MiniMax σε κάθε διαθέσιμη θέση (αναδρομή) 
4) Αξιολογεί κάθε αναδρομή με μια τιμή 
5) Επιστρέφει την βέλτιστη τιμή 
Υπάρχουν 8 δυνατοί συνδυασμοί για να κερδίσει κανείς :  
3 οριζόντια (κατά μήκος των γραμμών του πίνακα) 
3 κάθετα (κατά μήκος των στηλών του πίνακα) 
2 διαγώνια (οι 2 διαγώνιοι του 3x3 πίνακα) 
Υπάρχουν 3n^2 πιθανοί τρόποι με τους οποίους μπορούν να συμπληρωθούν τα κελιά-θέσεις, 
Όπου n η διάσταση του τετραγωνικού πίνακα. Άρα για έναν πίνακα 3x3 υπάρχουν                
19.683 διαφορετικοί πιθανοί τρόποι!  
Η υλοποιήση του κώδικα έγινε με τα παρακάτω βήματα: 
1) Δημιουργία 3x3 πίνακα και αρχικοποιήσή του με κενά 
2) Μετατροπή του πίνακα σε πλέγμα κουμπιών που είναι clickable από τον χρήστη 
3) Ορισμός μεταβλητών και αρχικές συνθήκες 
Π.χ ο χρήστης είναι ο ‘Ο’ , ο υπολογιστής είναι ο ‘Χ’ 
Ο χρήστης είναι ο Minimizer, ο υπολογιστής είναι ο Maximizer 
Για νίκη του χρήστη η τιμή που ορίζουμε είναι το -1, για την ήττα του χρήστη(νίκη του 
υπολογιστή) ορίζουμε το 1 ενώ για την ισοπαλία ορίζουμε το 0. 
4) Στη συνέχεια φτιάχνουμε τις συναρτήσεις για τη δημιουργία του παιχνιδιού - Συνάρτηση is_win(symbol):  
Παίρνει ως παράμετρο τον παίκτη-σύμβολο και ελέγχει αν πληρούνται  
συνθήκες νίκης. Στην ουσία ελέγχει αν στον πίνακα υπάρχει το ίδιο  
σύμβολο σε  3 κελιά-θέσεις του πίνακα, οριζόντια, κάθετα ή διαγώνια. -Συνάρτηση is_full(): 
οι 
Ελέγχει αν οι θέσεις του πίνακα είναι όλες κατειλημμένες ή υπάρχουν κενά. 
Στην ουσία είναι ο ‘διακόπτης’ του παιχνιδιού: αν δεν υπάρχουν κενά το παιχνίδι 
έχει τελειώσει αλλιώς το παιχνίδι συνεχίζεται. -Συνάρτηση evaluate(): 
Ελέγχει ποιος έχει κερδίσει όταν βρισκόμαστε σε μια τελική κατάσταση και 
επιστρέφει την τιμή -1, 1, 0. -Συνάρτηση minimax(is_maximizing): 
Παίρνει ως παράμετρο την boolean τιμή True αν ο τωρινός παίκτης είναι ο 
maximizer(Χ) και την τιμή False αν είναι ο minimizer(Ο). 
Αν ο τωρινός παίκτης είναι ο maximizer(X) η συνάρτηση ψάχνει όλες τις πιθανές 
κινήσεις καλώντας αναδρομικά τον εαυτό της για τον minimizer(O) και 
επιστρέφει την μέγιστη τιμή. 
Αν ο τωρινός παίκτης είναι ο minimizer(O) η συνάρτηση ψάχνει πάλι όλες τις 
πιθανές κινήσεις στον πίνακα, καλεί τον εαυτό της αναδρομικά για τον 
maximizer(X) και επιστρέφει την ελάχιστη τιμή. -Συνάρτηση find_best_move(): 
Η συνάρτηση αυτήν ανατρέχει σε όλες τις κενές θέσεις του πίνακα, κάνει μια 
κίνηση για τον υπολογιστή(Χ) και καλεί την συνάρτηση minimax για να  
αξιολογήσει την κάθε κίνηση. Στη συνέχει επιστρέφει την κίνηση με την  
μεγαλύτερη αξία( αφού ο υπολογιστής είναι ο maximizer).  -Συνάρτηση make_user_move(i): 
Παίρνει ως παράμετρο την θέση i του πίνακα στην οποία κλικάραμε, ελέγχει αν 
είναι άδεια και τοποθετεί το σύμβολο μας(Ο). Έπειτα ελέγχει αν κερδίσαμε ή 
αν  
υπάρχει ισοπαλία και αν όχι καλεί τον υπολογιστή να κάνει την κίνηση του. -Συνάρτηση make_computer_move(): 
Ελέγχει αν στον πίνακα υπάρχουν άδειες θέσεις, καλεί την συνάρτηση  
find_best_move για να βρεί την καλύτερη θέση για τον υπολογιστή(μέγιστη 
τιμή) και την τοποθετεί στον πίνακα. Ελέγχει αν κερδίζει ο υπολογιστής ή 
αν υπάρχει ισοπαλία και εμφανίζει στην οθόνη τα κατάλληλα μηνύματα. 
Για το γραφικό περιβάλλον του παιχνιδιού χρησιμοποιήθηκε η βιβλιοθήκη tkinter της 
python που είναι η πιο συνηθισμένη και user friendly για GUI. 