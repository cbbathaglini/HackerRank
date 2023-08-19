public static List<Integer> circularArrayRotation(List<Integer> a, int k, List<Integer> queries) {
    
    int n = a.size();
    List<Integer> arr_aux = new ArrayList<>();

    for(int i=0; i<k; i++){
        a.add(0,a.get(n-1));
        a.remove(n);
    }
            
    for(int i=0; i<queries.size(); i++){
        arr_aux.add(a.get(queries.get(i)));
    }
    return arr_aux;

}