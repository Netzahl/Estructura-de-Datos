package rankingSorts;

import java.awt.*;
import java.util.*;
import java.util.List;
import javax.swing.*;
import javax.swing.border.EmptyBorder;

public class ranking extends JFrame {

    // --- Componentes UI Principales ---
    private JTextArea resultsTextArea;  // Panel de texto para resultados
    private JPanel chartPanel;          // Panel donde se dibujará el gráfico
    private JDialog processingDialog;   // Diálogo modal "Procesando..."

    /**
     * Punto de entrada principal.
     * Crea y muestra la ventana principal en el hilo de despacho de eventos de Swing.
     */
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            ranking frame = new ranking();
            frame.setVisible(true);
        });
    }

    /**
     * Constructor. Configura la ventana principal del JFrame.
     */
    public ranking() {
        setTitle("Ranking de Algoritmos de Ordenamiento");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(1200, 800);
        setLocationRelativeTo(null);

        JPanel mainPanel = new JPanel(new BorderLayout());
        setContentPane(mainPanel);

        // Configurar los componentes de la UI
        setupUI(mainPanel);
        
        // Configurar el diálogo de "procesando"
        setupProcessingDialog();
    }

    /**
     * Construye la interfaz de usuario principal (botón, panel de texto y panel de gráfico).
     */
    private void setupUI(JPanel mainPanel) {
        // Botón para iniciar el benchmark
        JButton startButton = new JButton("Iniciar Benchmark (Seleccionar Escenario)");
        startButton.setFont(new Font("Arial", Font.BOLD, 16));
        startButton.addActionListener(e -> menu());
        mainPanel.add(startButton, BorderLayout.NORTH);

        // Área de texto para mostrar los resultados numéricos
        resultsTextArea = new JTextArea();
        resultsTextArea.setEditable(false);
        resultsTextArea.setFont(new Font("Monospaced", Font.PLAIN, 12));
        JScrollPane textScrollPane = new JScrollPane(resultsTextArea);
        textScrollPane.setPreferredSize(new Dimension(350, 700));

        // Panel que contendrá el gráfico de barras
        chartPanel = new JPanel();
        chartPanel.setLayout(new BorderLayout());
        
        // Panel dividido para texto y gráfico
        JSplitPane splitPane = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT, textScrollPane, chartPanel);
        splitPane.setDividerLocation(380);
        
        mainPanel.add(splitPane, BorderLayout.CENTER);
    }

    /**
     * Pre-configura el diálogo modal que se mostrará durante el procesamiento.
     */
    private void setupProcessingDialog() {
        processingDialog = new JDialog(this, "Procesando...", true); // Modal
        JLabel label = new JLabel("Ejecutando benchmarks, por favor espere...");
        label.setBorder(new EmptyBorder(20, 40, 20, 40));
        processingDialog.add(label);
        processingDialog.pack();
        processingDialog.setLocationRelativeTo(this);
    }

    /**
     * Muestra el menú (un JOptionPane) para que el usuario seleccione el escenario.
     */
    public void menu() {
        // Opciones de selección
        JComboBox<Integer> sizeComboBox = new JComboBox<>(new Integer[]{100, 1000, 10000, 100000});
        JComboBox<String> orderComboBox = new JComboBox<>(new String[]{"Ordenado", "Mediamente Ordenado", "Inverso"});

        // Panel para el diálogo de selección
        JPanel panel = new JPanel(new GridLayout(0, 2, 5, 5));
        panel.add(new JLabel("Tamaño del Arreglo:"));
        panel.add(sizeComboBox);
        panel.add(new JLabel("Pre-Orden del Arreglo:"));
        panel.add(orderComboBox);

        int result = JOptionPane.showConfirmDialog(this, panel, "Seleccionar Escenario de Prueba", 
                                                   JOptionPane.OK_CANCEL_OPTION, JOptionPane.PLAIN_MESSAGE);

        if (result == JOptionPane.OK_OPTION) {
            int n = (Integer) sizeComboBox.getSelectedItem();
            String orderType = (String) orderComboBox.getSelectedItem();
            
            // Limpiar resultados anteriores
            resultsTextArea.setText("Iniciando prueba para " + n + " elementos (" + orderType + ")...\n");
            chartPanel.removeAll();
            
            // Iniciar el procesamiento en segundo plano
            procesamiento(n, orderType);
        }
    }

    /**
     * Inicia el SwingWorker que ejecutará el benchmark en segundo plano.
     */
    public void procesamiento(int n, String orderType) {
        // Mostrar el diálogo "Procesando..."
        SwingUtilities.invokeLater(() -> processingDialog.setVisible(true));
        
        // Usar SwingWorker para ejecutar las tareas pesadas fuera del Hilo de Despacho de Eventos (EDT)
        class BenchmarkWorker extends SwingWorker<Map<String, Long>, String> {
            
            /**
             * El trabajo pesado se hace aquí, en un hilo de fondo.
             */
            @Override
            protected Map<String, Long> doInBackground() throws Exception {
                Map<String, Long> results = new LinkedHashMap<>();
                String[] algoritmos = {
                    "Bubble Sort", "Insertion Sort", "Selection Sort", 
                    "Shell Sort", "Merge Sort", "Quick Sort", 
                    "Heap Sort", "Radix Sort", "Bucket Sort"
                };

                publish("Generando arreglo base de " + n + " elementos...\n");
                int[] arrBase;
                switch (orderType) {
                    case "Ordenado":
                        arrBase = GeneradorArreglos.crearOrdenado(n);
                        break;
                    case "Mediamente Ordenado":
                        arrBase = GeneradorArreglos.crearMediamenteOrdenado(n);
                        break;
                    case "Inverso":
                    default:
                        arrBase = GeneradorArreglos.crearInverso(n);
                        break;
                }
                
                for (String algo : algoritmos) {
                    // *** SALVAGUARDA DE SEGURIDAD ***
                    // Saltar algoritmos O(n^2) para N >= 10,000 porque tardarían horas/días.
                    if ((algo.equals("Bubble Sort") || algo.equals("Insertion Sort") || algo.equals("Selection Sort")) && n > 10000) {
                        publish("Saltando " + algo + " (demasiado lento para N=" + n + ")...\n");
                        results.put(algo, -1L); // -1 significa "saltado"
                        continue;
                    }
                    
                    // QuickSort (pivote simple) es O(n^2) en arreglos ordenados/inversos
                    if (algo.equals("Quick Sort") && (orderType.equals("Ordenado") || orderType.equals("Inverso")) && n > 50000) {
                        publish("Saltando " + algo + " (riesgo de StackOverflow para N=" + n + ")...\n");
                        results.put(algo, -2L); // -2 significa "error/stack overflow"
                        continue;
                    }
                    
                    publish("Ejecutando " + algo + "...");
                    
                    // Siempre usar una copia fresca del arreglo base
                    int[] arrCopia = Arrays.copyOf(arrBase, arrBase.length);
                    long startTime = System.nanoTime();
                    
                    try {
                        switch (algo) {
                            case "Bubble Sort": AlgoritmosOrdenamiento.bubbleSort(arrCopia); break;
                            case "Insertion Sort": AlgoritmosOrdenamiento.insertionSort(arrCopia); break;
                            case "Selection Sort": AlgoritmosOrdenamiento.selectionSort(arrCopia); break;
                            case "Shell Sort": AlgoritmosOrdenamiento.shellSort(arrCopia); break;
                            case "Merge Sort": AlgoritmosOrdenamiento.mergeSort(arrCopia); break;
                            case "Quick Sort": AlgoritmosOrdenamiento.quickSort(arrCopia); break;
                            case "Heap Sort": AlgoritmosOrdenamiento.heapSort(arrCopia); break;
                            case "Radix Sort": AlgoritmosOrdenamiento.radixSort(arrCopia); break;
                            case "Bucket Sort": AlgoritmosOrdenamiento.bucketSort(arrCopia); break;
                        }
                    } catch (StackOverflowError e) {
                        // Capturar error común de QuickSort
                        publish("¡ERROR en " + algo + "! StackOverflowError\n");
                        results.put(algo, -2L); // -2 significa "error"
                        continue;
                    } catch (Exception e) {
                        publish("¡ERROR en " + algo + "! " + e.getMessage() + "\n");
                        results.put(algo, -2L); // -2 significa "error"
                        continue;
                    }
                    
                    long endTime = System.nanoTime();
                    long durationNs = endTime - startTime;
                    results.put(algo, durationNs);
                    publish("...Completado (" + convertirNsATexto(durationNs) + ")\n");
                }
                return results;
            }

            /**
             * Publica actualizaciones de progreso en el EDT.
             */
            @Override
            protected void process(List<String> chunks) {
                for (String text : chunks) {
                    resultsTextArea.append(text);
                }
            }

            /**
             * Se ejecuta en el EDT cuando doInBackground() termina.
             */
            @Override
            protected void done() {
                try {
                    // Obtener los resultados del hilo de fondo
                    Map<String, Long> results = get();
                    
                    // Mostrar resultados en el panel de texto
                    mostrarResumenTexto(results, n, orderType);
                    
                    // Generar y mostrar el gráfico
                    grafica(results, n, orderType);

                } catch (Exception e) {
                    resultsTextArea.append("\n¡Error durante el benchmark! " + e.getMessage());
                    e.printStackTrace();
                } finally {
                    // Ocultar el diálogo "Procesando..."
                    processingDialog.setVisible(false);
                }
            }
        }
        
        // Iniciar el worker
        new BenchmarkWorker().execute();
    }

    /**
     * Muestra el resumen de resultados ordenados en el JTextArea.
     */
    private void mostrarResumenTexto(Map<String, Long> results, int n, String orderType) {
        // Ordenar los resultados por tiempo (de mejor a peor)
        ArrayList<Map.Entry<String, Long>> sortedResults = new ArrayList<>(results.entrySet());
        
        // Comparador personalizado: -1 (saltado) y -2 (error) van al final
        sortedResults.sort((e1, e2) -> {
            long v1 = e1.getValue();
            long v2 = e2.getValue();
            if (v1 < 0 && v2 < 0) return 0;
            if (v1 < 0) return 1;  // v1 es malo, va al final
            if (v2 < 0) return -1; // v2 es malo, va al final
            return Long.compare(v1, v2); // Orden ascendente normal
        });

        resultsTextArea.append("\n--- Resumen por Escenario ---\n");
        resultsTextArea.append("Escenario: " + n + " elementos (" + orderType + ")\n");
        resultsTextArea.append("Resultados (de mejor a peor):\n");
        
        for (Map.Entry<String, Long> entry : sortedResults) {
            String algo = entry.getKey();
            long timeNs = entry.getValue();
            String timeStr;
            
            if (timeNs == -1L) {
                timeStr = "SALTADO (N^2)";
            } else if (timeNs == -2L) {
                timeStr = "ERROR (p.ej. StackOverflow)";
            } else {
                timeStr = convertirNsATexto(timeNs);
            }
            resultsTextArea.append(String.format("  %-16s: %s\n", algo, timeStr));
        }
    }

    /**
     * Prepara y muestra el panel del gráfico.
     */
    public void grafica(Map<String, Long> results, int n, String orderType) {
        String titulo = "Resultados: " + n + " elementos (" + orderType + ")";
        
        // Filtrar resultados negativos (saltados/error) antes de graficar
        Map<String, Long> validResults = new LinkedHashMap<>();
        for (Map.Entry<String, Long> entry : results.entrySet()) {
            if (entry.getValue() >= 0) {
                // Asegurarse de que no haya tiempos de 0 ns para la escala logarítmica
                validResults.put(entry.getKey(), Math.max(1, entry.getValue())); // Mínimo 1 ns
            }
        }
        
        GraficaResultados panelGrafica = new GraficaResultados(validResults, titulo);
        
        chartPanel.removeAll();
        chartPanel.add(panelGrafica, BorderLayout.CENTER);
        chartPanel.revalidate();
        chartPanel.repaint();
    }
    
    /**
     * Helper para formatear nanosegundos a un formato legible (ns, µs, ms, s).
     */
    private String convertirNsATexto(long ns) {
        if (ns < 1000) { return ns + " ns"; }
        if (ns < 1_000_000) { return String.format("%.3f µs", ns / 1000.0); }
        if (ns < 1_000_000_000) { return String.format("%.3f ms", ns / 1_000_000.0); }
        return String.format("%.3f s", ns / 1_000_000_000.0);
    }
    
    // --- CLASES INTERNAS ESTÁTICAS ---
    // Ponerlas dentro de la clase 'ranking' las mantiene en un solo archivo
    // pero organizadas lógicamente.

    /**
     * Generador de arreglos de prueba.
     */
    static class GeneradorArreglos {
        /**
         * Genera un arreglo de N elementos en orden ascendente.
         */
        public static int[] crearOrdenado(int n) {
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = i + 1;
            }
            return arr;
        }

        /**
         * Genera un arreglo de N elementos en orden descendente.
         */
        public static int[] crearInverso(int n) {
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = n - i;
            }
            return arr;
        }

        /**
         * Genera un arreglo ordenado y luego mezcla un 20% de sus elementos.
         */
        public static int[] crearMediamenteOrdenado(int n) {
            int[] arr = crearOrdenado(n);
            Random rand = new Random();
            int intercambios = n / 5; // 20% de intercambios

            for (int i = 0; i < intercambios; i++) {
                int idx1 = rand.nextInt(n);
                int idx2 = rand.nextInt(n);
                
                int temp = arr[idx1];
                arr[idx1] = arr[idx2];
                arr[idx2] = temp;
            }
            return arr;
        }
    }

    /**
     * Implementación de los 9 algoritmos de ordenamiento.
     * Todos los métodos modifican el arreglo "in-place".
     */
    static class AlgoritmosOrdenamiento {

        // 1. Bubble Sort
        public static void bubbleSort(int[] arr) {
            int n = arr.length;
            boolean swapped;
            for (int i = 0; i < n - 1; i++) {
                swapped = false;
                for (int j = 0; j < n - 1 - i; j++) {
                    if (arr[j] > arr[j + 1]) {
                        int temp = arr[j];
                        arr[j] = arr[j + 1];
                        arr[j + 1] = temp;
                        swapped = true;
                    }
                }
                if (!swapped) break;
            }
        }

        // 2. Insertion Sort
        public static void insertionSort(int[] arr) {
            for (int i = 1; i < arr.length; i++) {
                int key = arr[i];
                int j = i - 1;
                while (j >= 0 && arr[j] > key) {
                    arr[j + 1] = arr[j];
                    j--;
                }
                arr[j + 1] = key;
            }
        }

        // 3. Selection Sort
        public static void selectionSort(int[] arr) {
            int n = arr.length;
            for (int i = 0; i < n - 1; i++) {
                int minIdx = i;
                for (int j = i + 1; j < n; j++) {
                    if (arr[j] < arr[minIdx]) {
                        minIdx = j;
                    }
                }
                int temp = arr[minIdx];
                arr[minIdx] = arr[i];
                arr[i] = temp;
            }
        }

        // 4. Shell Sort (con secuencia de gaps de Knuth)
        public static void shellSort(int[] arr) {
            int n = arr.length;
            int h = 1;
            while (h < n / 3) {
                h = 3 * h + 1;
            }
            while (h >= 1) {
                for (int i = h; i < n; i++) {
                    int key = arr[i];
                    int j = i;
                    while (j >= h && arr[j - h] > key) {
                        arr[j] = arr[j - h];
                        j -= h;
                    }
                    arr[j] = key;
                }
                h /= 3;
            }
        }

        // 5. Merge Sort
        public static void mergeSort(int[] arr) {
            if (arr.length < 2) return;
            int mid = arr.length / 2;
            int[] left = Arrays.copyOfRange(arr, 0, mid);
            int[] right = Arrays.copyOfRange(arr, mid, arr.length);
            
            mergeSort(left);
            mergeSort(right);
            merge(arr, left, right);
        }

        private static void merge(int[] arr, int[] left, int[] right) {
            int i = 0, j = 0, k = 0;
            while (i < left.length && j < right.length) {
                if (left[i] <= right[j]) {
                    arr[k++] = left[i++];
                } else {
                    arr[k++] = right[j++];
                }
            }
            while (i < left.length) arr[k++] = left[i++];
            while (j < right.length) arr[k++] = right[j++];
        }

        // 6. Quick Sort (pivote simple)
        public static void quickSort(int[] arr) {
            quickSort(arr, 0, arr.length - 1);
        }

        private static void quickSort(int[] arr, int low, int high) {
            if (low < high) {
                int pi = partition(arr, low, high);
                quickSort(arr, low, pi - 1);
                quickSort(arr, pi + 1, high);
            }
        }

        private static int partition(int[] arr, int low, int high) {
            int pivot = arr[high];
            int i = low - 1;
            for (int j = low; j < high; j++) {
                if (arr[j] < pivot) {
                    i++;
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
            int temp = arr[i + 1];
            arr[i + 1] = arr[high];
            arr[high] = temp;
            return i + 1;
        }

        // 7. Heap Sort
        public static void heapSort(int[] arr) {
            int n = arr.length;
            // Construir max-heap
            for (int i = n / 2 - 1; i >= 0; i--) {
                heapify(arr, n, i);
            }
            // Extraer elementos uno por uno
            for (int i = n - 1; i > 0; i--) {
                int temp = arr[0];
                arr[0] = arr[i];
                arr[i] = temp;
                heapify(arr, i, 0); // Re-heapificar el montículo reducido
            }
        }

        private static void heapify(int[] arr, int n, int i) {
            int largest = i;
            int left = 2 * i + 1;
            int right = 2 * i + 2;
            if (left < n && arr[left] > arr[largest]) largest = left;
            if (right < n && arr[right] > arr[largest]) largest = right;
            if (largest != i) {
                int swap = arr[i];
                arr[i] = arr[largest];
                arr[largest] = swap;
                heapify(arr, n, largest);
            }
        }

        // 8. Radix Sort (LSD)
        public static void radixSort(int[] arr) {
            if (arr.length == 0) return;
            int max = Arrays.stream(arr).max().getAsInt();
            for (int exp = 1; max / exp > 0; exp *= 10) {
                countingSortByDigit(arr, exp);
            }
        }

        private static void countingSortByDigit(int[] arr, int exp) {
            int n = arr.length;
            int[] output = new int[n];
            int[] count = new int[10]; // Dígitos 0-9
            
            for (int i = 0; i < n; i++) {
                count[(arr[i] / exp) % 10]++;
            }
            
            for (int i = 1; i < 10; i++) {
                count[i] += count[i - 1];
            }
            
            for (int i = n - 1; i >= 0; i--) {
                output[count[(arr[i] / exp) % 10] - 1] = arr[i];
                count[(arr[i] / exp) % 10]--;
            }
            
            System.arraycopy(output, 0, arr, 0, n);
        }

        // 9. Bucket Sort
        public static void bucketSort(int[] arr) {
            if (arr.length <= 0) return;

            // 1. Encontrar max y min
            int max = arr[0], min = arr[0];
            for (int val : arr) {
                max = Math.max(max, val);
                min = Math.min(min, val);
            }

            // 2. Crear buckets
            // Usaremos n/10 buckets, con un mínimo de 1.
            int numBuckets = Math.max(1, arr.length / 10);
            List<Integer>[] buckets = new ArrayList[numBuckets];
            for (int i = 0; i < numBuckets; i++) {
                buckets[i] = new ArrayList<>();
            }

            // 3. Distribuir elementos en buckets
            long rango = (long) max - min + 1;
            for (int val : arr) {
                int bucketIndex = (int) (((long) val - min) * numBuckets / rango);
                // Asegurarse de que el índice esté dentro de los límites (especialmente para el valor max)
                if (bucketIndex >= numBuckets) bucketIndex = numBuckets - 1;
                buckets[bucketIndex].add(val);
            }

            // 4. Ordenar buckets individuales
            for (List<Integer> bucket : buckets) {
                // Usar Insertion Sort (o Collections.sort)
                Collections.sort(bucket);
            }

            // 5. Concatenar buckets de nuevo en el arreglo
            int index = 0;
            for (List<Integer> bucket : buckets) {
                for (int val : bucket) {
                    arr[index++] = val;
                }
            }
        }
    }

    /**
     * Un JPanel personalizado que dibuja un gráfico de barras LOGARÍTMICO.
     * Esto es esencial para comparar tiempos que varían por órdenes de magnitud.
     */
    static class GraficaResultados extends JPanel {
        private Map<String, Long> results;
        private String titulo;
        private Color[] colors;

        public GraficaResultados(Map<String, Long> results, String titulo) {
            this.results = results;
            this.titulo = titulo;
            this.colors = new Color[results.size()];
            
            // Generar colores aleatorios pero bonitos (alta saturación, alto brillo)
            Random rand = new Random();
            for (int i = 0; i < colors.length; i++) {
                colors[i] = Color.getHSBColor(rand.nextFloat(), 0.7f, 0.9f);
            }
            setBackground(Color.WHITE);
        }

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            Graphics2D g2 = (Graphics2D) g;
            g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

            if (results == null || results.isEmpty()) {
                g2.drawString("No hay datos para graficar.", 50, 50);
                return;
            }

            int padding = 60;
            int labelPadding = 120;
            int width = getWidth() - padding - labelPadding;
            int height = getHeight() - 2 * padding;
            int barHeight = height / (results.size() * 2); // Dejar espacio entre barras

            // Encontrar el tiempo máximo (para la escala)
            long maxTimeNs = 1; // Empezar en 1 para evitar log(0)
            for (long time : results.values()) {
                maxTimeNs = Math.max(maxTimeNs, time);
            }
            
            // Usar escala logarítmica
            double maxLogTime = Math.log10(maxTimeNs);

            // Título
            g2.setFont(new Font("Arial", Font.BOLD, 16));
            g2.drawString(titulo, padding, padding / 2);

            // Eje X (logarítmico)
            g2.setFont(new Font("Arial", Font.PLAIN, 10));
            g2.drawLine(labelPadding, height + padding, width + labelPadding, height + padding);
            
            // Dibujar marcas de escala logarítmica (1ns, 1µs, 1ms, 1s, ...)
            String[] units = {"1 ns", "10 ns", "100 ns", "1 µs", "10 µs", "100 µs", "1 ms", "10 ms", "100 ms", "1 s"};
            for (int i = 0; i < units.length; i++) {
                long timeNs = (long) Math.pow(10, i);
                if (timeNs > maxTimeNs * 1.1) break;
                
                double logTime = Math.log10(timeNs);
                int x = labelPadding + (int) (width * (logTime / maxLogTime));
                g2.drawLine(x, height + padding - 5, x, height + padding + 5);
                g2.drawString(units[i], x - 10, height + padding + 20);
            }

            // Dibujar barras
            int i = 0;
            int y = padding + barHeight;
            g2.setFont(new Font("Arial", Font.PLAIN, 12));

            for (Map.Entry<String, Long> entry : results.entrySet()) {
                long timeNs = entry.getValue();
                double logTime = Math.log10(timeNs);
                int barWidth = (int) (width * (logTime / maxLogTime));

                // Dibujar etiqueta (nombre del algoritmo)
                g2.setColor(Color.BLACK);
                g2.drawString(entry.getKey(), padding / 2, y + barHeight / 2);

                // Dibujar barra
                g2.setColor(colors[i]);
                g2.fillRect(labelPadding, y, barWidth, barHeight);
                
                // Dibujar valor (tiempo)
                g2.setColor(Color.DARK_GRAY);
                String timeString = convertirNsATexto(timeNs);
                g2.drawString(timeString, labelPadding + barWidth + 5, y + barHeight / 2 + 5);

                y += 2 * barHeight;
                i++;
            }
        }
        
        // Helper de conversión de tiempo local para el gráfico
        private String convertirNsATexto(long ns) {
            if (ns < 1000) return ns + " ns";
            if (ns < 1_000_000) return String.format("%.1f µs", ns / 1000.0);
            if (ns < 1_000_000_000) return String.format("%.2f ms", ns / 1_000_000.0);
            return String.format("%.3f s", ns / 1_000_000_000.0);
        }
    }
}