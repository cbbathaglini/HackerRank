public static List<Integer> permutationEquation(List<Integer> p) {
        List<Integer> arr_final = new ArrayList<>();
    
        for(int i=0; i<p.size();i++){
            arr_final.add(p.indexOf(p.indexOf(i+1)+1)+1);
        }
        return arr_final;

    }