import SwiftUI

struct ContentView: View {
    // MARK: - States
    
    @State private var topCount = 0
    @State private var bottomCount = 0
    @State private var timerIsRunning = false
    @State private var elapsedTime = 0.0
    @State private var timer = Timer.publish(every: 0.1, on: .main, in: .common).autoconnect()
    
    // MARK: - Calculations
    
    var total: Int {
        return topCount + bottomCount
    }
    
    var effectiveness: Double {
        guard total > 0 else {
            return 0
        }
        return Double(topCount) / Double(total) * 100
    }
    
    var rate: Double {
        guard elapsedTime > 0 else {
            return 0
        }
        let ratePerHour = Double(total) / (elapsedTime / 3600)
        return ratePerHour
    }
    
    var formattedTime: String {
        let minutes = Int(elapsedTime) / 60
        let seconds = Int(elapsedTime) % 60
        let milliseconds = Int(elapsedTime * 10) % 10
        return String(format: "%02d:%02d.%01d", minutes, seconds, milliseconds)
    }
    
    @Environment(\.colorScheme) var colorScheme
    
    // MARK: - Body
    
    var body: some View {
        GeometryReader { geometry in
            VStack {
                // Timer Section
                HStack {
                    Text(formattedTime)
                        .font(.headline)
                        .foregroundColor(colorScheme == .dark ? .white : .black)
                        .padding(.leading, 16)
                        .onReceive(timer) { _ in
                            if timerIsRunning {
                                elapsedTime += 0.1
                            }
                        }
                    
                    Spacer()
                    
                    // Reset Button
                    Button(action: {
                        resetCounts()
                    }) {
                        Image(systemName: "arrow.counterclockwise")
                            .font(.title)
                            .foregroundColor(.blue)
                    }
                    .padding()
                }
                
                // Rate Section
                Text("Rate: \(String(format: "%.2f", rate)) per hour")
                    .font(.headline)
                    .foregroundColor(colorScheme == .dark ? .white : .black)
                    .padding(.leading, 16)
                
                Spacer()
                
                VStack(spacing: 0) {
                    Spacer()
                    
                    // PASS Button
                    Button(action: {
                        topCount += 1
                    }) {
                        VStack {
                            Text("PASS")
                                .font(.headline)
                                .foregroundColor(colorScheme == .dark ? .white : .green)
                                .padding(.vertical, 8)
                            
                            Text("\(topCount)")
                                .font(.system(size: 60))
                                .foregroundColor(colorScheme == .dark ? .white : .black)
                                .padding()
                        }
                        .frame(width: geometry.size.width * 0.8, height: geometry.size.height * 0.4)
                        .overlay(
                            RoundedRectangle(cornerRadius: 10)
                                .stroke(colorScheme == .dark ? Color.white : Color.green, lineWidth: 2)
                        )
                    }
                    
                    Spacer()
                        .frame(height: 24)
                    
                    // FAIL Button
                    Button(action: {
                        bottomCount += 1
                    }) {
                        VStack {
                            Text("FAIL")
                                .font(.headline)
                                .foregroundColor(colorScheme == .dark ? .white : .red)
                                .padding(.vertical, 8)
                            
                            Text("\(bottomCount)")
                                .font(.system(size: 60))
                                .foregroundColor(colorScheme == .dark ? .white : .black)
                                .padding()
                        }
                        .frame(width: geometry.size.width * 0.8, height: geometry.size.height * 0.4)
                        .overlay(
                            RoundedRectangle(cornerRadius: 10)
                                .stroke(colorScheme == .dark ? Color.white : Color.red, lineWidth: 2)
                        )
                    }
                    
                    Spacer()
                }
                .padding(.horizontal)
                
                // Total and Effectiveness Section
                HStack {
                    Text("Total: \(total)")
                        .font(.headline)
                        .foregroundColor(colorScheme == .dark ? .white : .black)
                        .padding(.leading, 16)
                    
                    Spacer()
                    
                    Text("Effectiveness: \(String(format: "%.2f", effectiveness))%")
                        .font(.headline)
                        .foregroundColor(colorScheme == .dark ? .white : .black)
                        .padding(.trailing, 16)
                }
                
                Spacer()
            }
        }
        .onTapGesture {
            timerIsRunning.toggle()
        }
        .onReceive(NotificationCenter.default.publisher(for: UIApplication.willResignActiveNotification)) { _ in
            timerIsRunning = false
        }
    }
    
    // MARK: - Private Methods
    
    private func resetCounts() {
        topCount = 0
        bottomCount = 0
        elapsedTime = 0.0
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
