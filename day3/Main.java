import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    private static String[] GRID;
    private static int H, W;
    private static Map<List<Integer>, List<Integer>> COORDS;

    public static void main(String[] args) {
        readInputFile("./input");
        findMatches();
        findAndStoreSymbols();
        System.out.println(partOne());
        System.out.println(partTwo());
    }

    private static void readInputFile(String filePath) {
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            List<String> gridLines = new ArrayList<>();
            String line;
            while ((line = br.readLine()) != null) {
                gridLines.add(line);
            }
            GRID = gridLines.toArray(new String[0]);
            H = GRID.length;
            W = GRID[0].length();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void findMatches() {
        Pattern pattern = Pattern.compile("(\\d+)");
        List<List<Pair<Integer, Pair<Integer, Integer>>>> matches = new ArrayList<>();

        for (String line : GRID) {
            Matcher matcher = pattern.matcher(line);
            List<Pair<Integer, Pair<Integer, Integer>>> lineMatches = new ArrayList<>();

            while (matcher.find()) {
                int value = Integer.parseInt(matcher.group(1));
                Pair<Integer, Integer> span = new Pair<>(matcher.start(), matcher.end() - 1);
                lineMatches.add(new Pair<>(value, span));
            }

            matches.add(lineMatches);
        }

        COORDS = new HashMap<>();

        for (int y = 0; y < H; y++) {
            List<Pair<Integer, Pair<Integer, Integer>>> line = matches.get(y);
            for (Pair<Integer, Pair<Integer, Integer>> match : line) {
                int part = match.getLeft();
                Pair<Integer, Integer> span = match.getRight();
                List<Integer> key = findSymbol(y, span.getLeft(), span.getRight());
                if (key != null) {
                    COORDS.computeIfAbsent(key, k -> new ArrayList<>()).add(part);
                }
            }
        }
    }

    private static List<Integer> findSymbol(int y, int x1, int x2) {
        for (int v = y - 1; v <= y + 1; v++) {
            for (int u = x1 - 1; u <= x2 + 1; u++) {
                if (v >= 0 && v < H && u >= 0 && u < W && GRID[v].charAt(u) != '.' && !Character.isDigit(GRID[v].charAt(u))) {
                    return List.of(v, u);
                }
            }
        }
        return null;
    }

    private static void findAndStoreSymbols() {
        for (Map.Entry<List<Integer>, List<Integer>> entry : COORDS.entrySet()) {
            System.out.println("Coordinate: " + entry.getKey() + ", Parts: " + entry.getValue());
        }
    }

    private static int partOne() {
        return COORDS.values().stream().flatMap(List::stream).mapToInt(Integer::intValue).sum();
    }

    private static int partTwo() {
        return COORDS.values().stream()
            .filter(parts -> parts.size() >= 2)  
            .map(parts -> parts.get(0) * parts.get(1))
            .mapToInt(Integer::intValue)
            .sum();
    }

    static class Pair<L, R> {
        private final L left;
        private final R right;

        public Pair(L left, R right) {
            this.left = left;
            this.right = right;
        }

        public L getLeft() {
            return left;
        }

        public R getRight() {
            return right;
        }
    }
}

