from fastapi import APIRouter, Response
from models.response import ImageAsset

endpoint = APIRouter(prefix="/api")

@endpoint.get('/image/assets', response_model=dict[str, list[ImageAsset]])
async def get_image_assets(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"

    return {
        "Low Quality": [
            {
                "name": "Ventje Rahardjo",
                "position": "Direktur Eksekutif",
                "photo": "/storage/upload/thumb/1672130209-ventje-rahadjo-soedigno.png"
            },
            {
                "name": "Afdhal Aliasar",
                "position": "Direktur Industri Produk Halal",
                "photo": "/storage/upload/thumb/1672130201-afdhal-aliasar.png"
            },
            {
                "name": "Taufik Hidayat",
                "position": "Direktur Jasa Keuangan Syariah",
                "photo": "/storage/upload/thumb/1672130188-taufiq-hidayat.png"
            },
            {
                "name": "Ahmad Juwaini",
                "position": "Direktur Keuangan Sosial Syariah",
                "photo": "/storage/upload/thumb/1672130178-ahmad-juwaini.png"
            },
            {
                "name": "Putu Rahwidhiyasa",
                "position": "Direktur Bisnis dan Kewirausahaan Syariah",
                "photo": "/storage/upload/thumb/1597624639-Putu Rahwidhiyasacircle.png"
            },
            {
                "name": "Sutan Emir Hidayat",
                "position": "Direktur Infrastruktur Ekosistem Syariah",
                "photo": "/storage/upload/thumb/1672130164-sutan-emir-hidayat.png"
            },
            {
                "name": "Presiden RI",
                "position": "Ketua",
                "photo": "/storage/upload/thumb/1672129110-presiden.png"
            },
            {
                "name": "Wakil Presiden RI",
                "position": "Ketua Harian",
                "photo": "/storage/upload/thumb/1672129933-wakil-presiden.png"
            },
            {
                "name": "Kementerian Keuangan",
                "position": "Sekertaris",
                "photo": "/storage/upload/thumb/1672130266-img-kemenkeu.png"
            },
            {
                "name": "Kominte Nasional Ekonomi dan Keuangan Syariah",
                "position": "Manajemen Eksekutif",
                "photo": "/storage/upload/thumb/1672130481-img-knks_old_0721a.png"
            },
            {
                "name": "Anggota",
                "position": "Anggota",
                "photo": "/storage/upload/thumb/1672135174-anggota.png"
            }
        ], "High Quality": [
            {
                "name": "Ventje Rahardjo",
                "position": "Direktur Eksekutif",
                "photo": "/storage/upload/1672130209-ventje-rahadjo-soedigno.png"
            },
            {
                "name": "Afdhal Aliasar",
                "position": "Direktur Industri Produk Halal",
                "photo": "/storage/upload/1672130201-afdhal-aliasar.png"
            },
            {
                "name": "Taufik Hidayat",
                "position": "Direktur Jasa Keuangan Syariah",
                "photo": "/storage/upload/1672130188-taufiq-hidayat.png"
            },
            {
                "name": "Ahmad Juwaini",
                "position": "Direktur Keuangan Sosial Syariah",
                "photo": "/storage/upload/1672130178-ahmad-juwaini.png"
            },
            {
                "name": "Putu Rahwidhiyasa",
                "position": "Direktur Bisnis dan Kewirausahaan Syariah",
                "photo": "/storage/upload/1597624639-Putu Rahwidhiyasacircle.png"
            },
            {
                "name": "Sutan Emir Hidayat",
                "position": "Direktur Infrastruktur Ekosistem Syariah",
                "photo": "/storage/upload/1672130164-sutan-emir-hidayat.png"
            },
            {
                "name": "Presiden RI",
                "position": "Ketua",
                "photo": "/storage/upload/1672129110-presiden.png"
            },
            {
                "name": "Wakil Presiden RI",
                "position": "Ketua Harian",
                "photo": "/storage/upload/1672129933-wakil-presiden.png"
            },
            {
                "name": "Kementerian Keuangan",
                "position": "Sekertaris",
                "photo": "/storage/upload/1672130266-img-kemenkeu.png"
            },
            {
                "name": "Kominte Nasional Ekonomi dan Keuangan Syariah",
                "position": "Manajemen Eksekutif",
                "photo": "/storage/upload/1672130481-img-knks_old_0721a.png"
            },
            {
                "name": "Anggota",
                "position": "Anggota",
                "photo": "/storage/upload/1672135174-anggota.png"
            }
        ]
    }