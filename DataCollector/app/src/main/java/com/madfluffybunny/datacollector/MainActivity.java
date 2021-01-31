package com.madfluffybunny.datacollector;

import android.Manifest;
import android.content.Context;
import android.content.pm.PackageManager;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.provider.ContactsContract;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.Switch;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.ToggleButton;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;

import static android.os.Environment.getExternalStorageDirectory;
import static android.util.Half.EPSILON;
import static java.lang.Math.cos;
import static java.lang.Math.sin;
import static java.lang.Math.sqrt;

public class MainActivity extends AppCompatActivity implements SensorEventListener {
    SensorManager sensorManager;
    Sensor acce;
    Sensor gyro;
    int DataCount = 0;
    BufferedWriter out;
    BufferedWriter out_accuracy_acce;
    BufferedWriter out_gyro;
    BufferedWriter out_accuracy_gyro;

    final float alpha = (float) 0.8;
    private static final float NS2S = 1.0f / 1000000000.0f;
    private final float[] deltaRotationVector = new float[4];
    private float timestamp;

    private static final int STORAGE_PERMISSION_CODE = 101;

    public void checkPermission(String permission, int requestCode)
    {
        if (ContextCompat.checkSelfPermission(MainActivity.this, permission)
                == PackageManager.PERMISSION_DENIED) {

            // Requesting the permission
            ActivityCompat.requestPermissions(MainActivity.this,
                    new String[] { permission },
                    requestCode);
        }
        else {
            Toast.makeText(MainActivity.this,
                    "Permission already granted",
                    Toast.LENGTH_SHORT)
                    .show();
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
// Function to check and request permission.

        checkPermission(
                Manifest.permission.WRITE_EXTERNAL_STORAGE,
                STORAGE_PERMISSION_CODE);
        checkPermission(
                Manifest.permission.READ_EXTERNAL_STORAGE,
                STORAGE_PERMISSION_CODE);
        try {
            out = new BufferedWriter(new FileWriter(getExternalStorageDirectory()+"/accelerometer.csv", true));
        } catch (IOException e) {
            e.printStackTrace();
        }
//
//        try {
//            out_accuracy_acce = new BufferedWriter(new FileWriter(getExternalStorageDirectory()+"/accuracy_accelerometer.csv", true));
//        } catch (IOException e) {
//            e.printStackTrace();
//        }

        try {
            out_gyro= new BufferedWriter(new FileWriter(getExternalStorageDirectory()+"/gyro.csv", true));
        } catch (IOException e) {
            e.printStackTrace();
        }

//        try {
//            out_accuracy_gyro= new BufferedWriter(new FileWriter(getExternalStorageDirectory()+"/accuracy_gyro.csv", true));
//        } catch (IOException e) {
//            e.printStackTrace();
//        }


        SensorManager sensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        List<Sensor> deviceSensors = sensorManager.getSensorList(Sensor.TYPE_ALL);
        System.out.println(deviceSensors);
        Log.e("SENSOR", deviceSensors.get(0).toString());

//        acce = deviceSensors.get(0);
//        gyro = deviceSensors.get(2);

        acce = sensorManager.getDefaultSensor(Sensor.TYPE_LINEAR_ACCELERATION);

        gyro = sensorManager.getDefaultSensor(Sensor.TYPE_ROTATION_VECTOR);


        if (acce == null){
            acce = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
        }

        if (gyro == null){
            gyro = sensorManager.getDefaultSensor(Sensor.TYPE_ORIENTATION);
        }

        Log.e("init", acce.toString());
        Log.e("init", gyro.toString());

        Switch toggle = (Switch) findViewById(R.id.switch1);
        toggle.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (isChecked) {
                    sensorManager.registerListener(MainActivity.this, acce, SensorManager.SENSOR_DELAY_FASTEST);
                } else {
                    sensorManager.unregisterListener(MainActivity.this);
                }
            }
        });


        Switch toggle2 = (Switch) findViewById(R.id.switch2);
        toggle2.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (isChecked) {
                    sensorManager.registerListener(MainActivity.this, gyro, SensorManager.SENSOR_DELAY_FASTEST);
                } else {
                    sensorManager.unregisterListener(MainActivity.this);
                }
            }
        });

        Switch toggle3 = (Switch) findViewById(R.id.switch3);
        toggle3.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (isChecked) {
                    sensorManager.registerListener(MainActivity.this, acce, SensorManager.SENSOR_DELAY_FASTEST);
                    sensorManager.registerListener(MainActivity.this, gyro, SensorManager.SENSOR_DELAY_FASTEST);
                } else {
                    sensorManager.unregisterListener(MainActivity.this);

                }
            }
        });


//        sensorManager.registerListener(this,acce, SensorManager.SENSOR_DELAY_FASTEST);
        Log.e("FILE LOCATION", String.valueOf(getFilesDir()));
        TextView location_info = findViewById(R.id.file_text);
        location_info.setText(String.valueOf(getFilesDir()));
    }

    @Override
    public final void onAccuracyChanged(Sensor sensor, int accuracy) {
//        try {
//            StringBuilder values = new StringBuilder();
//            values.append(DataCount);
//            values.append(',');
//            for (int i = 0; i < event.values.length; i++) {
//
//                values.append(event.values[i]);
//                values.append(',');
//            }
//            out.write(String.valueOf(values));
//            out.write('\n');
////                out.close();
//            Log.e("TESTING SAVING", String.valueOf(values));
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
    }

    @Override
    public final void onSensorChanged(SensorEvent event) {

        // The light sensor returns a single value.
        // Many sensors return 3 values, one for each axis.
        // Do something with this sensor value.

//        gravity[0] = alpha * gravity[0] + (1 - alpha) * event.values[0];
//        gravity[1] = alpha * gravity[1] + (1 - alpha) * event.values[1];
//        gravity[2] = alpha * gravity[2] + (1 - alpha) * event.values[2];
//
//        linear_acceleration[0] = event.values[0] - gravity[0];
//        linear_acceleration[1] = event.values[1] - gravity[1];
//        linear_acceleration[2] = event.values[2] - gravity[2];
        if (event.sensor == acce) {
            DataCount++;
            try {
                StringBuilder values = new StringBuilder();
                //int increment new data count
                values.append(DataCount);
                values.append(',');
                for (int i = 0; i < event.values.length; i++) {
                    //xyz?
                    values.append(event.values[i]);
                    values.append(',');
                }
                //accuracy
                values.append(event.accuracy);
                values.append(',');
                //time epoch
                values.append(event.timestamp);

                out.write(String.valueOf(values));
                out.write('\n');
//                out.close();
                Log.e("ACCELEROMETER DATA", String.valueOf(values));
            } catch (IOException e) {
                e.printStackTrace();
            }

        }else if(event.sensor == gyro){
            // This time step's delta rotation to be multiplied by the current rotation
            // after computing it from the gyro sample data.
//            long timestamp = 0;
//            if (timestamp != 0) {
//                final float dT = (event.timestamp - timestamp) * NS2S;
//                // Axis of the rotation sample, not normalized yet.
//                float axisX = event.values[0];
//                float axisY = event.values[1];
//                float axisZ = event.values[2];
//
//                // Calculate the angular speed of the sample
//                float omegaMagnitude = (float) sqrt(axisX*axisX + axisY*axisY + axisZ*axisZ);
//
//                // Normalize the rotation vector if it's big enough to get the axis
//                if (omegaMagnitude > EPSILON) {
//                    axisX /= omegaMagnitude;
//                    axisY /= omegaMagnitude;
//                    axisZ /= omegaMagnitude;
//                }
//
//                // Integrate around this axis with the angular speed by the time step
//                // in order to get a delta rotation from this sample over the time step
//                // We will convert this axis-angle representation of the delta rotation
//                // into a quaternion before turning it into the rotation matrix.
//                float thetaOverTwo = omegaMagnitude * dT / 2.0f;
//                float sinThetaOverTwo = (float) sin(thetaOverTwo);
//                float cosThetaOverTwo = (float) cos(thetaOverTwo);
//                deltaRotationVector[0] = sinThetaOverTwo * axisX;
//                deltaRotationVector[1] = sinThetaOverTwo * axisY;
//                deltaRotationVector[2] = sinThetaOverTwo * axisZ;
//                deltaRotationVector[3] = cosThetaOverTwo;
//            }
//
//            timestamp = event.timestamp;
//            float[] deltaRotationMatrix = new float[9];
//            SensorManager.getRotationMatrixFromVector(deltaRotationMatrix, deltaRotationVector);
//            // User code should concatenate the delta rotation we computed with the current
//            // rotation in order to get the updated rotation.
//            // rotationCurrent = rotationCurrent * deltaRotationMatrix;
            // TODO MAM PROBLEM NIE WIEM CO TUTAJ TRZEBA ZROBIC


            try {
                StringBuilder values = new StringBuilder();
                //count
                values.append(DataCount);
                values.append(',');
                for (int i = 0; i < event.values.length; i++) {
                    //values
                    values.append(event.values[i]);
                    values.append(',');
                }
                //accuracy
                values.append(event.accuracy);
                values.append(',');
                //timestamp
                values.append(event.timestamp);

                out_gyro.write(String.valueOf(values));
                out_gyro.write('\n');
//                out.close();
                Log.e("GYRO DATA", String.valueOf(values));
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

}